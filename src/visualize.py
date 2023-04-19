from PIL import Image, ImageDraw

class visualize:
    """Uses the Pillow package to visualization the dfs navigation
    """
    def __init__(self) -> None:
        self.pxls = 30
        self.borders = 6
        self.images = []
    
    def __drawOutlines(self, draw: ImageDraw) -> ImageDraw:
        pass

    def __drawPaths(self, thePath: list, draw: ImageDraw) -> ImageDraw:
        pass

    def drawMaze(self, thePath:list = []) -> None:
        """
        1. Intializes an image with the maze's dimensions with cell structure
        2. Draw the walls and paths
        3. The current path and store the list of images to memory
        """
        # 1.
        im = Image.new(
            'RGB', (self.pxls * len(self.maze[0]), self.pxls * len(self.maze)), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        # 2.
        draw = self.__drawOutlines(draw)
        # 3.
        draw = self.__drawPaths(thePath, draw)
        self.images.append(im)

