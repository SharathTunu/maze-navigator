from PIL import Image, ImageDraw

class visualize:
    """Uses the Pillow package to visualization the dfs navigation
    """
    def __init__(self) -> None:
        self.pxls = 30
        self.borders = 6
        self.images = []
    
    def __drawOutlines(self, draw: ImageDraw) -> ImageDraw:
        """
        1. Fill the walls with black and leave the paths white
        2. Add gray dots to the open path.
        """
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                color = (255, 255, 255)
                r = 0
                # 1.
                if self.maze[i][j] == 1:
                    color = (0, 0, 0)
                if [i,j] in [self.entrance, self.exit]:
                    color = (0, 255, 0)
                    r = self.borders
                
                draw.rectangle((j*self.pxls+r, i*self.pxls+r,
                                j*self.pxls+self.pxls-r-1, i*self.pxls+self.pxls-r-1), fill=color)
                # 2.
                if self.maze[i][j] == 2:
                    r = self.borders
                    draw.ellipse((j * self.pxls + r, i * self.pxls + r,
                                  j * self.pxls + self.pxls - r - 1, i * self.pxls + self.pxls - r - 1),
                                 fill=(128, 128, 128))
        return draw

    def __drawPaths(self, thePath: list, draw: ImageDraw) -> ImageDraw:
        """Connect the dots drawn above with lines that show the path explored by dfs
        """
        for u in range(len(thePath)-1):
            y = thePath[u][0]*self.pxls + int(self.pxls/2)
            x = thePath[u][1]*self.pxls + int(self.pxls/2)
            y1 = thePath[u+1][0]*self.pxls + int(self.pxls/2)
            x1 = thePath[u+1][1]*self.pxls + int(self.pxls/2)
            draw.line((x, y, x1, y1), fill=(255, 0, 0), width=5)
        return draw

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
    
    def save(self, im_path: str) -> None:
        self.images[0].save(im_path,
                save_all=True, append_images=self.images[1:],
                optimize=False, duration=50, loop=0)
        print(f"Visualization is available at {im_path} ...please open it to see the dfs in action.")

