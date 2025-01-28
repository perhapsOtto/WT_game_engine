

import math


class PhysicsComp():

    def __init__(self):
        #TODO: this one's gonna be fun...
        pass

    def move(self, objects, delta):
        for obj in objects:
            
            obj.move(delta)
            obj.gravity(delta)
            if obj.collision is not None:
                obj.collision.grounded = False
        self.process(objects, delta)

    def process(self, objects, delta, again = 3):
        unchecked = objects.copy()
        for obj in objects:
             #reset grounded (check and set later)
            #obj.check_sleep()
            #obj.move(delta)
            #obj.gravity(delta)
            if not obj.asleep and obj.collision is not None:
                unchecked.remove(obj)
                for obj2 in unchecked:
                    if obj is not obj2 and obj2.collision is not None:
                        self.collide(obj, obj2)
            #print(obj, obj.collision.grounded)
        #print("-_-_-_-_-")
        if again > 0:
            self.process(objects, 0.0, again-1)

    def resolve_r_r_col(self,obj1, obj2):
        #obj1_center = obj1.collision.center()
        #obj2_center = obj2.collision.center()
        
        shortest = abs(obj1.y - (obj2.y + obj2.collision.height))
        move_total = [0, -shortest] 
        if abs(obj2.y - (obj1.y + obj1.collision.height))<shortest:
            shortest = abs(obj2.y - (obj1.y + obj1.collision.height))
            move_total = [0, shortest]
        if abs(obj2.x - (obj1.x + obj1.collision.width))<shortest:
            shortest = abs(obj2.x - (obj1.x + obj1.collision.width))
            move_total = [shortest, 0]
        if abs(obj1.x - (obj2.x + obj2.collision.width))<shortest:
            shortest = abs(obj1.x - (obj2.x + obj2.collision.width))
            move_total = [-shortest, 0]
        move_1 = move_total.copy()
        move_2 = move_total.copy()
        if obj1.static:
            move_1 = [0, 0]
            move_2 = list(map(lambda x:x*2, move_2))
        if obj2.static:
            move_2 = [0, 0]
            move_1 = list(map(lambda x:x*2, move_1))
        obj1.x -= move_1[0]/2.0
        obj1.y -= move_1[1]/2.0
        obj1.old_velocity = [move_1[0]/2.0, move_1[1]/2.0]
        obj2.x += move_2[0]/2.0
        obj2.y += move_2[1]/2.0
        obj2.old_velocity = [move_2[0]/2.0, move_2[1]/2.0]

    
    def collide(self, obj1, obj2, resolve=True):
        match [obj1.collision.shape, obj2.collision.shape]:
            case ["RECT", "RECT"]:
                #check if in range vertically
                #check horiz
                #print("r-r")
                if (obj1.x+obj1.collision.width) > obj2.x and obj1.x < (obj2.x+obj2.collision.width):
                    if obj1.y-0.1<obj2.y+obj2.collision.height and obj1.y > obj2.y:
                        obj1.collision.grounded = True
                    if obj2.y-0.1<obj1.y+obj1.collision.height and obj2.y > obj1.y:
                        obj2.collision.grounded = True
                    if (obj1.y+obj1.collision.height) > obj2.y and obj1.y < (obj2.y+obj2.collision.height):
                        if resolve:
                            self.resolve_r_r_col(obj1, obj2)
                        return True
                return False
                            

                
            case ["RECT", "CIRC"]:
                print("r-c")
            case ["CIRC", "RECT"]:
                print("c-r")
            case ["CIRC", "CIRC"]:
                print("c-c")

    def dist(self, x1, y1, x2, y2):
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def slope(self, x1, y1, x2, y2):
        return [x2 - x1, y2 - y1]
