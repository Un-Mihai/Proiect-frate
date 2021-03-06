import turtle
t2 = turtle.Turtle()
t = turtle.Turtle()
s = turtle.getscreen()

t2.pensize(3)
d = 20
t2.speed(0)

def arcd():
    t2.rt(180)
    t2.circle(d,-90)
    t2.rt(180)

def arcs():
    t2.circle(d,90)

def dreptunghi(x,y,l,L,c):
    t2.pu()
    t2.goto(x,y)
    t2.pd()
    t2.fillcolor(c)
    t2.pencolor(c)
    t2.begin_fill()
    for i in range (2):
        t2.fd(l)
        arcd()
        t2.fd(L)
        arcd()
    t2.end_fill()

def telefon(x,y,l,L,c):
    dreptunghi(x,y,l,L,c)
    dreptunghi(x+d/2,y-d/2,l-d,L-2*d,"white")
    t2.pu()
    t2.goto(x+l/2,y-L-d)
    t2.pd()
    t2.dot(d/2)

def laptop(x,y,l,c):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.fillcolor(c)
    t.begin_fill()
    t.fd(4.5 * l)
    t.lt(115)
    t.fd(1.6 * l)
    t.lt(65)
    t.fd(3.2 * l)
    t.lt(65)
    t.fd(1.6 * l)
    t.end_fill()
    t.lt(180)
    t.pu()
    t.pensize(l/10)
    t.pencolor("white")
    t.fd(1.4 * l)
    n = 2.5
    for k in range(4):
        t.rt(65)
        t.fd(0.4 * l)
        t.pd()
        t.fd(n * l)
        t.pu()
        t.bk((n+0.4) * l)
        t.lt(65)
        t.bk(0.2 * l)
        n += 0.2
    t.pensize(1)
    t.fillcolor("white")
    t.bk(0.4 * l)
    t.rt(65)
    t.fd(1.8 * l)
    t.pd()
    t.fd(0.8 * l)
    t.lt(120)
    t.begin_fill()
    t.fd(0.4 * l)
    t.lt(60)
    t.fd(0.4 * l)
    t.lt(60)
    t.fd(0.4 * l)
    t.end_fill()
    t.pu()
    t.rt(60)
    t.fillcolor(c)
    #t.begin_fill()
    t.fd(1.8 * l)
    t.rt(115)
    t.fd(0.5 * l)
    t.rt(65)
    t.fd( 1.6 * l)
    t.rt(90)
    t.fd(0.45 * l)
    #t.end_fill()
    t.rt(90)
    t.fd(1.8 * l)
    t.rt(115)
    t.fd(1.4 * l)
    t.lt(25)
    t.fd(0.15 * l)
    t.pencolor("black")
    t.pd()
    t.begin_fill()
    for k in range(2):
        t.fd(1.9 * l)
        t.rt(90)
        t.fd(3.2 * l)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.fd(0.2 * l)
    t.rt(90)
    t.fd(0.2 * l)
    t.pd()
    t.fillcolor("white")
    t.begin_fill()
    for k in range(2):
        t.fd(2.8 * l)
        t.lt(90)
        t.fd(1.5 * l)
        t.lt(90)
    t.end_fill()

t2.pencolor("blue")
t2.pu()
t2.goto((3.5*d),(-19.5*d))
t2.pd()
t2.lt(90)
t2.fd(5*d)
arcd()
t2.fd(2*d)
arcs()
t2.fd(5*d)
arcd()
t2.fd(3*d)

#aici punem telefon
telefon(12.5*d,-3.5*d,2*d,4*d,"blue")

t2.pu()
t2.goto(11.5*d,-6.5*d)
t2.pd()
t2.pencolor("blue")
t2.fd(-2*d)
t2.rt(-90)
t2.fd(3*d)
t2.rt(90)

#aici punem telefon
telefon(8.5*d,2.5*d,2*d,4*d,"#3DEBEB")

t2.pencolor("blue")
t2.pu()
t2.fd(2.1*d)
t2.rt(-90)
t2.fd(2*d)
t2.rt(90)
t2.pd()
t2.fd(5.5*d)

#aici punem tableta
dreptunghi(17.5*d,1.5*d,4*d,2*d,"#7D1BA1")

t2.pencolor("blue")
t2.pu()
t2.fd(1.5*d)
t2.rt(-90)
t2.fd(0.1*d)
t2.pd()
t2.fd(3*d)
t2.rt(90)

#aici punem telefon
telefon(18.1*d,9.5*d,2*d,4*d,"#1F3EB8")
t2.rt(-90)

t2.pencolor("green")
t2.pu()
t2.goto((4.5*d),(-19.5*d))
t2.pd()
t2.fd(6*d)

t2.pencolor("#237F9E")
t2.pu()
t2.goto((2.5*d),(-19.5*d))
t2.pd()
t2.fd(9*d)
arcd()
t2.fd(3*d)
arcs()

t2.pencolor("#BFBA2C")
t2.pu()
t2.goto(2.5*d,-10.5*d)
t2.pd()
t2.fd(3*d)
arcd()
t2.fd(d)
arcs()
t2.fd(3*d)

t2.pencolor("#CC8B12")
t2.pu()
t2.goto((1.5*d),(-19.5*d))
t2.pd()
t2.fd(17*d)

#ecran tableta
t2.rt(90)
dreptunghi(18.5*d,d,2*d,d,"white")

#laptop
laptop(-4.5*d,-2.5*d,2.5*d,"orange")
