import turtle as trl
import emoji
from turtle import done

scr = trl.Screen()
scr.bgcolor('black')
scr.title('Dictionary')
scr.setup(width=1.0,height=1.0)
pen = trl.Turtle()
pen.speed(1)
pen.hideturtle()
pen.up()

pen.goto(-180,80)
pen.width(20)
pen.color('cyan')
pen.down()
pen.right(90)
pen.forward(100)
pen.up()

pen.left(90)
pen.forward(20)
pen.down()
pen.color('cyan')
pen.circle(65,215)

pen.up()
pen.goto(-88,-30)
pen.write('ictionary',font=('Ubuntu Mono',50,'bold'))

pen.up()
pen.goto(100,-50)
pen.color('white')
pen.write('Made by AU',font=('Ubuntu Mono',15))

done()