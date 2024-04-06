from abc import ABC, abstractmethod
from MoveType import MoverType

class Model(ABC):
    
    @abstractmethod
    def isOccupied(self) -> bool:
        pass
    
    @abstractmethod
    def isSolved(self) -> bool:
        pass
    
    @abstractmethod
    def getActivePuzzle(self) -> Puzzle:
        pass
    
    @abstractmethod
    def getActivePuzzleIndex() -> int:
        pass
    
    @abstractmethod 
    def setActivePuzzleIndex(self, index):
        pass
    
    @abstractmethod 
    def resetPuzzle(self):
        pass
    
    @abstractmethod
    def isMoveIllegal(self, r, c) -> bool:
        pass