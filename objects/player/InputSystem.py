from direct.showbase import DirectObject
from direct.task import Task
from panda3d.core import CollisionTraverser, CollisionHandlerQueue,\
                                CollisionNode, CollisionRay, GeomNode

class InputSystem (DirectObject.DirectObject):
    """
        Handles all input except for camera controls.
    """
    def __init__ (self):
        self._currentSelectedObject = None
        self._hoveredObject = None
        # Set up 'raycasting' for tile selection:
        self._picker = CollisionTraverser()
        self._queue = CollisionHandlerQueue()
        self._pickerNode = CollisionNode("mouseRay")
        self._pickerNP = base.cam.attachNewNode(self._pickerNode)
        self._pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
        self._pickerRay = CollisionRay()
        self._pickerNode.addSolid(self._pickerRay)
        self._picker.addCollider(self._pickerNP, self._queue)

        # Set up event and mouse control:
        self.accept("mouse1", self.selectObj)
        taskMgr.add(self._hoverSelectionTask, "hoverSelectionTask")

    def selectObj (self, selectObject=None):
        """
            Selects the given object. This is usually done when called from
             another place.
            Otherwise, selects the object mouse is hovering over.
        """
        if selectObject != None:
            self._currentSelectedObject = selectObject
        else:
            self._currentSelectedObject = self._hoveredObject
            #TODO: Play effects and stuff

    def _hoverSelectionTask (self, task):
        """
            Called every frame to highlight any selectable objects the player
             mouses over.
        """
        if base.mouseWatcherNode.hasMouse():
            mousePos = base.mouseWatcherNode.getMouse()
            newHoveredObject = self._getObjectRaycast(mousePos)
            # Set our stored hovered object as the hovered object:
            self._setHoveredObject(newHoveredObject) # Will work even if None!
        # Loop task indefinitely - every frame:
        return task.cont

    def _setHoveredObject(self, newHoveredObject):
        """
            Will highlight the newHoveredObject if it isn't the same as the last
             one. Removes highlight from the last Hovered Object.
            It will also update the stored hovered object to be the new.
        """
        if newHoveredObject != self._hoveredObject:
            #TODO Play highlight effects on new and remove effects from old
            self._hoveredObject = newHoveredObject

    def _getObjectRaycast(self, mousePos):
        """
            Given the mouse position, will determine if there is an object
             being hovered over.
            Returns this object, if it exists. Otherwise, returns None
        """
        # Point start ray from base camera and screen point.
        self._pickerRay.setFromLens(base.camNode, mousePos.getX(),
                                    mousePos.getY())
        self._picker.traverse(base.render) # Launch ray through render
        # If we have a hit, pick the closest one:
        if self._queue.getNumEntries() > 0:
            self._queue.sortEntries()
            pickedObject = self._queue.getEntry(0).getIntoNodePath()
            # Attempt to get the first selectable root object (if it exists):
            parentObject = pickedObject.getParent()
            while parentObject != base.render:
                if parentObject.getTag("selectable")=="true":
                    return parentObject
                else:
                    parentObject = parentObject.getParent()
        # Otherwise, none is auto returned.