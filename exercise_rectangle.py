def swap(a, b):
   return b, a

class Point:
   definition: str = "Abstract unit that represents a location in space"
   def __init__(self, given_x: float = 0, given_y: float = 0): # Initializer, simmilar to constructors
      # print("Initializer")
      self.x: float = given_x
      self.y: float = given_y
   def move(self, new_x, new_y):
      self.x = new_x
      self.y = new_y
   def reset(self):
      self.x = 0
      self.y = 0
   def compute_distance(self, point) -> float:
      return ((self.x - point.x))**0.5
   
class Segment:
   # * Class attributes are defined here (outside any method)
   def __init__(self, point1, point2) -> None:

      if point1.x < point2.x:
         self.start: Point = point1
         self.end: Point = point2
      else:
         self.start: Point = point2
         self.end: Point = point1

      self.associated_line = Line(self.start, self.end)
      self.type: str = self.define_type()
      self.length = self.compute_length()
      self.slope: float = self.compute_slope()
      self.x: float = 0.0
      self.b: float = 0.0

   def define_type(self):
      if (self.start.x - self.end.x) == 0.0:
         self.type = "vertical"
      
      elif (self.start.y - self.end.y) == 0.0:
         self.type = "horizontal"

      else:
         self.type = "oblique"

   def compute_length(self):
      return ((self.end.x - self.start.x)**2 + (self.end.y - self.start.y)**2)**0.5
   
   def compute_slope(self) -> float:
      if self.type == "vertical":
         return None
      
      elif self.type == "horizontal":
         return 0

      else:
         return (self.start.y - self.end.y) / (self.start.x - self.end.x)
      
   def compute_x_axis_cross(self) -> bool:
      if self.type == "horizontal":
         if (self.start.y == 0):
            return True
         else:
            return False
      else:
         if ((self.start.y <= 0) and (self.end.y >= 0)) or ((self.start.y >= 0) and (self.end.y <= 0)):
            return True
         else:
            return False
      
   def compute_y_axis_cross(self) -> bool:
      if self.type == "vertical":
         if (self.start.x == 0):
            return True
         else:
            return False
      else:
         if ((self.start.x >= 0) and (self.end.x <= 0)) or ((self.start.x <= 0) and (self.end.x >= 0)):
            return True
         else:
            return False
         
   def descretize_segment(self, n: int) -> list:
      self.descrete_points: list = [self.start]
      self.x_increment = (self.end.x - self.start.x) / (n - 1)
      i = self.start.x + self.x_increment
      while i < self.end.x:
         self.descrete_points.append(Point(round(i, 2), round((self.slope * i) + self.associated_line.b, 2)))
         i += self.x_increment
      self.descrete_points.append(self.end)
      print(self.slope)
      return self.descrete_points

class Line():
   def __init__(self, point1: Point, point2: Point) -> None:
      if point1.x < point2.x:
         self.start: Point = point1
         self.end: Point = point2
      else:
         self.start = point2
         self.end = point1

      self.slope: float = 0.0
      self.x: float = 0.0
      self.b: float = 0.0
      self.type: str = ""

      if (point1.x - point2.x) == 0.0:
         self.slope = None
         self.x = point1.x
         self.type = "vertical"
      
      elif (point1.y - point2.y) == 0.0:
         self.slope == 0.0
         self.b = point1.y
         self.type = "horizontal"
      else:
         self.slope = (point1.y - point2.y) / (point1.x - point2.x)
         self.b = point1.y - (self.slope * point1.x)
         self.type = "oblique"

class Rectangle:
   def __init__(self, method: int, *args) -> None:

      if method == 1:
         # Bottom-left corner Point
         self.center: Point = Point(given_x = args[0].x + (args[1] / 2), given_y = args[0].y + (args[2] / 2))
         self.width: float = args[1]
         self.height: float = args[2] 

      if method == 2:
         # Center point
         self.center: Point = args[0]
         self.width: float = args[1]
         self.height: float = args[2]

      if method == 3:
         #Opposite points
         self.center: Point = Point(given_x = (args[0].x + args[1].x) / 2, given_y = (args[0].y + args[1].y) / 2)
         if args[0].x < args[1].x:
               self.width: float = args[1].x - args[0].x #abs() ?
               self.height: float = args[1].y - args[0].y
         else:
               self.width: float = args[0].x - args[1].x
               self.height: float = args[0].y - args[1].y

      if method == 4:
         # Four segments
         segments: list = list(args)
         # The first two segments are vertical and the last two are horizontal

         if segments[0].start.x > segments[1].start.x:
            c = segments[0]
            segments[0] = segments[1]
            segments[1] = c
         if segments[2].start.y > segments[3].start.y:
            c = segments[2]
            segments[2] = segments[3]
            segments[3] = c

         self.center: Point = Point(given_x = (segments[1].start.x + segments[0].start.x)/2, given_y = (segments[3].start.y + segments[0].start.y)/2)
         self.width: float = segments[1].start.x - segments[0].start.x
         self.height: float = segments[3].start.y - segments[2].start.y

   def compute_area(self) -> float:
      return self.width * self.height
   
   def compute_perimeter(self) -> float:
      return (2 * self.width) + (2 * self.height)
   
   def compute_interference_point(self, point: Point) -> bool:
      if (point.x >= (self.center.x - (self.width/2)) and (point.x <= (self.center.x + (self.width/2)))) and (point.y >= (self.center.y - (self.height/2)) and (point.y <= (self.center.y + (self.height/2)))):
         return True
      else:
         return False
      
   def compute_interference_line (self, line: Line):
      self.top = self.center.y + (self.height / 2)
      self.bottom = self.center.y - (self.height / 2)
      self.left = self.center.x - (self.width / 2)
      self.right = self.center.x + (self.width / 2)
      cross_y_top: bool = False
      cross_y_bottom: bool = False
      cross_x_left: bool = False
      cross_x_right: bool = False
      conditions_met = []

      if line.type == "vertical":
         if (self.left <= line.x <= self.right):
            cross_y_bottom = True
            cross_y_top = True
      
      elif line.type == "horizontal":
         if (self.bottom <= line.slope <= self.top):
            cross_x_left = True
            cross_x_right = True

      else:
         cross_y_bottom = (self.left <= ((self.bottom - line.slope) / line.slope) <= self.right)
         cross_y_top = (self.left <= ((self.top - line.slope) / line.slope) <= self.right)
         cross_x_left = (self.bottom <= ((line.slope) * self.left) + line.slope <= self.top)
         cross_x_right = (self.bottom <= ((line.slope) * self.right) + line.slope <= self.top)

      conditions_met = [cross_y_bottom, cross_y_top, cross_x_left, cross_x_right]

      conditions_met = [x for x in conditions_met if (x == True)]
      if len(conditions_met) >= 2:
         print("The line crosses the rectangle")
      else:
         print("The line doesn't cross the rectangle")

   # def compute_interference_segment(self, segment: Segment):
   #    line_interference: bool = self.compute_interference_line(segment.associated_line)
   #    if line_interference == True:
   #       if (self.center.x - (self.width/2) <= segment.start.x <= self.center.x + (self.width/2)) or (self.center.x - (self.width/2) <= segment.end.x <= self.center.x + (self.width/2)):
   #          pass


class Square(Rectangle):
   def __init__(self, method: int, *args) -> None:
      if method == 1:
         super().__init__(1, args[0], args[1], args[1])
      elif method == 2:
         super().__init__(2, args[0], args[1], args[1])
      elif method == 3:
         super().__init__(3, args[0], args[1])
      else:
         super().__init__(4, args[0], args[1], args[2], args[3])

if __name__ == "__main__":
            
   print("Hello user!")
   method: int = int(input("Enter the method you want to use to create the rectangle (1, 2, 3 or 4): "))
   # ? Can you create an empty instance of an object?
   x: float = 0.0
   y: float = 0.0
   width: float = 0.0
   height: float = 0.0
   x1: float = 0.0
   y1: float = 0.0
   x2: float = 0.0
   y2: float = 0.0

   if method == 1:
      x = float(input("Enter the x coordinate of the bottom-left corner: "))
      y = float(input("Enter the y coordinate of the bottom-left corner: "))
      width = float(input("Enter the width of the rectangle: "))
      height = float(input("Enter the height of the rectangle: "))
      rectangle = Rectangle(1, Point(x, y), width, height)

   elif method == 2:
      x = float(input("Enter the x coordinate of the center: "))
      y = float(input("Enter the y coordinate of the center: "))
      width = float(input("Enter the width of the rectangle: "))
      height = float(input("Enter the height of the rectangle: "))
      rectangle = Rectangle(2, Point(x, y), width, height)

   elif method == 3:
      x1= float(input("Enter the x coordinate of the first point: "))
      y1= float(input("Enter the y coordinate of the first point: "))
      x2= float(input("Enter the x coordinate of the second point (opposite to the first one): "))
      y2= float(input("Enter the y coordinate of the second point: "))
      rectangle = Rectangle(3, Point(x1, y1), Point(x2, y2))
   
   elif method == 4:
      print("Create a rectangle using 4 segments: two vertical and two horizontal")
      x1 = float(input("Enter the x coordinate of the start point of the first vertical segment: "))
      y1 = float(input("Enter the y coordinate of the start point of the first vertical segment: "))
      y2 = float(input("Enter the y coordinate of the end point of the first vertical segment: "))
      vertical1 = Segment(Point(x1, y1), Point(x1, y2))

      x1 = float(input("Enter the x coordinate of the start point of the second vertical segment: "))
      vertical2 = Segment(Point(x1, y1), Point(x1, y2))
      horizontal1 = Segment(Point(vertical1.start.x, y1), Point(vertical2.start.x, y1))
      horizontal2 = Segment(Point(vertical1.end.x, y2), Point(vertical1.end.x, y2))
      rectangle = Rectangle(4, vertical1, vertical2, horizontal1, horizontal2)

   else:
      print("Invalid method")
   

   print("Now let's create a square")
   method: int = int(input("Enter the method you want to use to create the square (1, 2, or 3): "))
   if method == 1:
      x = float(input("Enter the x coordinate of the bottom-left corner: "))
      y = float(input("Enter the y coordinate of the bottom-left corner: "))
      width: float = float(input("Enter the length of the square's side: "))
      height: float = width
      square = Square(1, Point(x, y), width, height)

   elif method == 2:
      x = float(input("Enter the x coordinate of the center: "))
      y = float(input("Enter the y coordinate of the center: "))
      width: float = float(input("Enter the length of the square's side: "))
      height = width
      square = Square(2, Point(x, y), width, height)

   elif method == 3:
      x1 = float(input("Enter the x coordinate of the first point: "))
      y1 = float(input("Enter the y coordinate of the first point: "))
      x2 = float(input("Enter the x coordinate of the second point (opposite to the first one): "))
      y2 = float(input("Enter the y coordinate of the second point: "))
      square = Square(3, Point(x1, y1), Point(x2, y2))

   elif method == 4:
      print("Create a rectangle using 4 segments: two vertical and two horizontal")
      x1: float = float(input("Enter the x coordinate of the start point of the first vertical segment: "))
      y1: float = float(input("Enter the y coordinate of the start point of the first vertical segment: "))
      y2: float = float(input("Enter the y coordinate of the end point of the first vertical segment: "))
      vertical1 = Segment(Point(x1, y1), Point(x1, y2))
      vertical2 = Segment(Point(x1 + y1 - y2, y1), Point(x1 + y1 - y2, y2))
      horizontal1 = Segment(Point(vertical1.start.x, y1), Point(vertical2.start.x, y1))
      horizontal2 = Segment(Point(vertical2.end.x, y2), Point(vertical2.end.x, y2))
      
      square = Square(4, vertical1, vertical2, horizontal1, horizontal2)
   
   else:
      print("Invalid method")


   print("Now, let's create a point")
   x = float(input("Enter the x coordinate of the point: "))
   y = float(input("Enter the y coordinate of the point: "))
   point = Point(x, y)
   print(rectangle.compute_interference_point(point))

   print("Now let's create a line")
   x1 = float(input("Enter the x coordinate of the first point: "))
   y1 = float(input("Enter the y coordinate of the first point: "))
   x2 = float(input("Enter the x coordinate of the second point: "))
   y2 = float(input("Enter the y coordinate of the second point: "))
   line = Line(Point(x1, y1), Point(x2, y2))

   print("Now lets's create a segment")
   x1 = float(input("Enter the x coordinate of the first point: "))
   y1 = float(input("Enter the y coordinate of the first point: "))
   x2 = float(input("Enter the x coordinate of the second point: "))
   y2 = float(input("Enter the y coordinate of the second point: "))
   segment = Segment(Point(x1, y1), Point(x2, y2))
   n = float(input("Enter the number of points to descretize the segment: "))
   descrete_segments = segment.descretize_segment(n)
   i = 0
   while i < len(descrete_segments):
      print("(", descrete_segments[i].x, ", ", descrete_segments[i].y, ")")
      i += 1

   print(rectangle.compute_interference_line(line))

               