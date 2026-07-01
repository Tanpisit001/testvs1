"""
เกมงูกินหาง (Snake Game)
ควบคุมด้วยปุ่มลูกศร W A S D หรือ Arrow Keys
กด Space เพื่อเริ่มเกมใหม่หลังแพ้
"""

import turtle
import time
import random

# ---------- ตั้งค่าหน้าจอ ----------
screen = turtle.Screen()
screen.title("เกมงูกินหาง 🐍")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)  # ปิด auto update เพื่อควบคุม animation เอง

# ---------- ตัวแปรเกม ----------
delay = 0.1
score = 0
high_score = 0

# ---------- หัวงู ----------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ---------- อาหาร ----------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# ---------- ตัวหนังสือแสดงคะแนน ----------
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("คะแนน: 0  คะแนนสูงสุด: 0", align="center",
          font=("Courier", 18, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)


def reset_game():
    global delay, score, segments
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    score = 0
    delay = 0.1
    pen.clear()
    pen.write("คะแนน: {}  คะแนนสูงสุด: {}".format(score, high_score),
              align="center", font=("Courier", 18, "normal"))


# ---------- ผูกปุ่มควบคุม ----------
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# ---------- ลูปหลักของเกม ----------
while True:
    screen.update()

    # ชนขอบจอ -> แพ้
    if (head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290):
        if score > high_score:
            high_score = score
        reset_game()

    # กินอาหาร
    if head.distance(food) < 20:
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # เพิ่มลำตัวงู
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001  # เกมเร็วขึ้นทีละนิด
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("คะแนน: {}  คะแนนสูงสุด: {}".format(score, high_score),
                  align="center", font=("Courier", 18, "normal"))

    # ขยับลำตัวงูตามหัว (จากท้ายไปหน้า)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # ชนตัวเอง -> แพ้
    for segment in segments:
        if segment.distance(head) < 20:
            if score > high_score:
                high_score = score
            reset_game()

    time.sleep(delay)
