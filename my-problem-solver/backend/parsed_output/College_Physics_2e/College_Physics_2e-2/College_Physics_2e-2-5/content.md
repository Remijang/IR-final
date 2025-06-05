# 2.5 Motion Equations for Constant Acceleration in One Dimension

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Calculate displacement of an object that is not accelerating, given initial position and velocity. Calculate final velocity of an accelerating object, given initial velocity, acceleration, and time. Calculate displacement and final position of an accelerating object, given initial position, initial velocity, time, and acceleration.

We might know that the greater the acceleration of, say, a car moving away from a stop sign, the greater the displacement in a given time. But we have not developed a specific equation that relates acceleration and displacement. In this section, we develop some convenient equations for kinematic relationships, starting from the definitions of displacement, velocity, and acceleration already covered.

# Notation: $t , x , v , a$

First, let us make some simplifications in notation. Taking the initial time to be zero, as if time is measured with a stopwatch, is a great simplification. Since elapsed time is $\Delta t = t _ { \mathrm { f } } - t _ { 0 }$ , taking $t _ { 0 } = 0$ means that $\Delta t = t _ { \mathrm { f } }$ , the final time on the stopwatch. When initial time is taken to be zero, we use the subscript 0 to denote initial values of position and velocity. That is, $x _ { 0 }$ istheinitialpositionand $v _ { 0 }$ istheinitialvelocity. We put no subscripts on the final values. That is, $t$ isthefinaltime, $x$ isthefinalposition, and $v$ isthefinalvelocity. This gives a simpler expression for elapsed time—now, $\Delta t = t$ . It also simplifies the expression for displacement, which is now $\Delta x = x - x _ { 0 }$ . Also, it simplifies the expression for change in velocity, which is now $\Delta v = v - v _ { 0 }$ . To summarize, using the simplified notation, with the initial time taken to be zero,

$$
\left. \begin{array} { l } { \Delta t } \\ { \Delta x } \\ { \Delta v } \end{array} \right\} \left. \begin{array} { r } { t } \\ { \Delta x } \\ { v - v _ { 0 } } \end{array} \right\}
$$

wherethesubscript0denotesaninitialvalueandtheabsenceofasubscriptdenotesafinalvalue in whatever motion is under consideration.

We now make the important assumption that ac elerationisconstant. This assumption allows us to avoid using calculus to find instantaneous acceleration. Since acceleration is constant, the average and instantaneous accelerations are equal. That is,

$$
\overline { { { a } } } = a = { \mathrm { c o n s t a n t } } ,
$$

so we use the symbol for acceleration at all times. Assuming acceleration to be constant does not seriously limit the situations we can study nor degrade the accuracy of our treatment. For one thing, acceleration isconstant in a great number of situations. Furthermore, in many other situations we can accurately describe motion by assuming a constant acceleration equal to the average acceleration for that motion. Finally, in motions where acceleration changes drastically, such as a car accelerating to top speed and then braking to a stop, the motion can be considered in separate parts, each of which has its own constant acceleration.

# Solving for Displacement $( \Delta x )$ and Final Position $\pmb { \left( x \right) }$ from Average Velocity when Acceleration ( ) is Constant

To get our first two new equations, we start with the definition of average velocity:

$$
{ \boldsymbol { \overline { { v } } } } = { \frac { \Delta x } { \Delta t } } .
$$

Substituting the simplified notation for $\Delta x$ and $\Delta t$ yields

$$
{ \overline { { v } } } = { \frac { x - x _ { 0 } } { t } } .
$$

Solving for $x$ yields

$$
x = x _ { 0 } + \overline { { v } } t ,
$$

where the average velocity is

$$
\overline { { { v } } } = \frac { v _ { 0 } + v } { 2 } ( \mathrm { c o n s t a n t } a ) .
$$

The equation r eflects the fact that, when acceleration is constant, $v$ is just the simple average of the initial and final velocities. For example, if you steadily increase your velocity (that is, with constant acceleration) from 30 to $6 0 ~ \mathsf { k m / h }$ , then your average velocity during this steady increase is $4 5 k m / \mathsf { h }$ . Using the equation $\begin{array} { r } { \overline { { v } } = \frac { v _ { 0 } + v } { 2 } } \end{array}$ to check this, we see that

$$
\overline { { v } } = \frac { v _ { 0 } + v } { 2 } = \frac { 3 0 \mathrm { k m / h } + 6 0 \mathrm { k m / h } } { 2 } = 4 5 \mathrm { k m / h } ,
$$

which seems logical.

# EXAMPLE 2.8

# Calculating Displacement: How Far does the Jogger Run?

A jogger runs down a straight stretch of road with an average velocity of $4 . 0 0 ~ \mathrm { m } / \mathsf { s }$ for 2.00 min. What is his final position, taking his initial position to be zero?

# Strategy

Draw a sketch.

The final position $x$ is given by the equation

$$
x = x _ { 0 } + \overline { { v } } t .
$$

To find $x$ , we identify the values of $x _ { 0 }$ , $\overline { { v } }$ , and $t$ from the statement of the problem and substitute them into the equation.

# Solution

1. Identify the knowns. $\overline { { v } } = 4 . 0 0 \mathrm { m / s }$ , $\Delta t = 2 . 0 0 \mathrm { m i n }$ , and $x _ { 0 } = 0 \mathrm { m }$ .

2. Enter the known values into the equation.

$$
x = x _ { 0 } + \overline { { v } } t = 0 + ( 4 . 0 0 \mathrm { m / s } ) ( 1 2 0 \mathrm { s } ) = 4 8 0 \mathrm { m }
$$

# Discussion

Velocity and final displacement are both positive, which means they are in the same direction.

The equation $x = x _ { 0 } + \overline { { v } } t$ gives insight into the relationship between displacement, average velocity, and time. It shows, for example, that displacement is a linear function of average velocity. (By linear function, we mean that displacement depends on $\overline { { v } }$ rather than on $\overline { { v } }$ raised to some other power, such as $\overline { { v } } ^ { 2 }$ . When graphed, linear functions look like straight lines with a constant slope.) On a car trip, for example, we will get twice as far in a given time if we average $9 0 ~ \mathrm { k m / h }$ than if we average $4 5 k m / \mathsf { h }$ .

# Solving for Final Velocity

We can derive another useful equation by manipulating the definition of acceleration.

$$
a = { \frac { \Delta v } { \Delta t } }
$$

Substituting the simplified notation for $\Delta v$ and $\Delta t$ gives us

$$
a = { \frac { v - v _ { 0 } } { t } } ( \mathrm { c o n s t a n t } a ) .
$$

Solving for $v$ yields

$$
v = v _ { 0 } + a t ( \mathrm { c o n s t a n t } a ) .
$$

# EXAMPLE 2.9

# Calculating Final Velocity: An Airplane Slowing Down after Landing

An airplane lands with an initial velocity of $7 0 . 0 ~ \mathsf { m } / \mathsf { s }$ and then decelerates at $1 . 5 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ for $4 0 . 0 \mathsf s .$ . What is its final velocity?

# Strategy

Draw a sketch. We draw the acceleration vector in the direction opposite the velocity vector because the plane is decelerating.

# Solution

1. Identify the knowns. $v _ { 0 } = 7 0 . 0 \mathrm { m / s }$ , $a = - 1 . 5 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ , $t = 4 0 . 0 ~ \mathrm { s }$ .   
2. Identify the unknown. In this case, it is final velocity, $v _ { \mathrm { f } }$ .   
3. Determine which equation to use. We can calculate the final velocity using the equation $v = v _ { 0 } + a t$ .

4. Plug in the known values and solve.

$$
v = v _ { 0 } + a t = 7 0 . 0 ~ \mathrm { m / s } + \left( - 1 . 5 0 ~ \mathrm { m / s ^ { 2 } } \right) ( 4 0 . 0 ~ \mathrm { s } ) = 1 0 . 0 ~ \mathrm { m / s }
$$

# Discussion

The final velocity is much less than the initial velocity, as desired when slowing down, but still positive. With jet engines, reverse thrust could be maintained long enough to stop the plane and start moving it backward. That would be indicated by a negative final velocity, which is not the case here.

In addition to being useful in problem solving, the equation $v = v _ { 0 } + a t$ gives us insight into the relationships among velocity, acceleration, and time. From it we can see, for example, that

• final velocity depends on how large the acceleration is and how long it lasts   
• if the acceleration is zero, then the final velocity equals the initial velocity $( v = v _ { 0 } )$ , as expected (i.e., velocity is constant)   
• if is negative, then the final velocity is less than the initial velocity

(All of these observations fit our intuition, and it is always useful to examine basic equations in light of our intuition and experiences to check that they do indeed describe nature accurately.)

# Making Connections: Real-World Connection

An intercontinental ballistic missile (ICBM) has a larger average acceleration than the Space Shuttle and achieves a greater velocity in the first minute or two of flight (actual ICBM burn times are classified—short-burntime missiles are more difficult for an enemy to destroy). But the Space Shuttle obtains a greater final velocity, so that it can orbit the earth rather than come directly back down as an ICBM does. The Space Shuttle does this by accelerating for a longer time.

# Solving for Final Position When Velocity is Not Constant $\textstyle \left( a \neq 0 \right)$ )

We can combine the equations above to find a third equation that allows us to calculate the final position of an object experiencing constant acceleration. We start with

$$
v = v _ { 0 } + a t .
$$

Adding $v _ { 0 }$ to each side of this equation and dividing by 2 gives

$$
\frac { v _ { 0 } + v } { 2 } = v _ { 0 } + \frac 1 2 a t .
$$

Since $\begin{array} { r } { \frac { v _ { 0 } + v } { 2 } = \overline { { v } } } \end{array}$ for constant acceleration, then

$$
\overline { { { v } } } = v _ { 0 } + \frac { 1 } { 2 } a t .
$$

Now we substitute this expression for $\overline { { v } }$ into the equation for displacement, $x = x _ { 0 } + \overline { { v } } t$ , yielding

$$
x = x _ { 0 } + v _ { 0 } t + { \frac { 1 } { 2 } } a t ^ { 2 } \ ( { \mathrm { c o n s t a n t } } \ a ) .
$$

# EXAMPLE 2.10

# Calculating Displacement of an Accelerating Object: Dragsters

Dragsters can achieve average accelerations of $2 6 . 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ . Suppose such a dragster accelerates from rest at this rate for 5.56 s. How far does it travel in this time?

# Strategy

Draw a sketch.

We are asked to find displacement, which is $x$ if we take $x _ { 0 }$ to be zero. (Think about it like the starting line of a race. It can be anywhere, but we call it 0 and measure all other positions relative to it.) We can use the equation $\begin{array} { r } { x = x _ { 0 } + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } } \end{array}$ once we identify $v _ { 0 }$ , $a$ , and $t$ from the statement of the problem.

# Solution

1. Identify the knowns. Starting from rest means that $v _ { 0 } = 0$ , $a$ is given as $2 6 . 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ and $t$ is given as 5.56 s.

2. Plug the known values into the equation to solve for the unknown $x$ :

$$
x = x _ { 0 } + v _ { 0 } t + { \frac { 1 } { 2 } } a t ^ { 2 } .
$$

Since the initial position and velocity are both zero, this simplifies to

$$
x = { \frac { 1 } { 2 } } a t ^ { 2 } .
$$

Substituting the identified values of $a$ and $t$ gives

$$
x = \frac { 1 } { 2 } \big ( 2 6 . 0 \mathrm { m / s } ^ { 2 } \big ) ( 5 . 5 6 \mathrm { s } ) ^ { 2 } ,
$$

yielding

$$
x = 4 0 2 { \mathrm { m } } .
$$

# Discussion

If we convert $4 0 2 ~ \mathsf { m }$ to miles, we find that the distance covered is very close to one quarter of a mile, the standard distance for drag racing. So the answer is reasonable. This is an impressive displacement in only $5 . 5 6 \ : \mathsf { s }$ , but topnotch dragsters can do a quarter mile in even less time than this.

What else can we learn by examining the equation $\begin{array} { r } { x = x _ { 0 } + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } \ ? } \end{array}$ We see that:

• displacement depends on the square of the elapsed time when acceleration is not zero. In Example 2.10, the dragster covers only one fourth of the total distance in the first half of the elapsed time   
• if acceleration is zero, then the initial velocity equals average velocity $( v _ { 0 } = \overline { { v } } )$ and $\begin{array} { r } { x = x _ { 0 } + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } } \end{array}$ becomes $x = x _ { 0 } + v _ { 0 } t$

# Solving for Final Velocity when Velocity Is Not Constant $( a \neq 0 ]$ )

A fourth useful equation can be obtained from another algebraic manipulation of previous equations.

If we solve $v = v _ { 0 } + a t$ for $t$ , we get

$$
t = { \frac { v - v _ { 0 } } { a } } .
$$

Substituting this and $\begin{array} { r } { \overline { { \boldsymbol { v } } } = \frac { v _ { 0 } + v } { 2 } } \end{array}$ into $x = x _ { 0 } + \overline { { v } } t$ , we get

$$
v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } ) ( { \mathrm { c o n s t a n t } } a ) .
$$

# EXAMPLE 2.11

# Calculating Final Velocity: Dragsters

Calculate the final velocity of the dragster in Example 2.10 without using information about time.

# Strategy

Draw a sketch.

The equation $v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } )$ is ideally suited to this task because it relates velocities, acceleration, and displacement, and no time information is required.

# Solution

1. Identify the known values. We know that $v _ { 0 } = 0$ , since the dragster starts from rest. Then we note that $x - x _ { 0 } = 4 0 2 \mathrm { m }$ (this was the answer in Example 2.10). Finally, the average acceleration was given to be $a = 2 6 . 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ .

2. Plug the knowns into the equation $v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } )$ and solve for $v$ .

$$
v ^ { 2 } = 0 + 2 \bigl ( 2 6 . 0 \mathrm { m / s } ^ { 2 } \bigr ) ( 4 0 2 \mathrm { m } ) .
$$

Thus

$$
v ^ { 2 } = 2 . 0 9 \times 1 0 ^ { 4 } \mathrm { \ m } ^ { 2 } / \mathrm { s } ^ { 2 } .
$$

To get $v$ , we take the square root:

$$
v = { \sqrt { 2 . 0 9 \times 1 0 ^ { 4 } ~ { \mathrm { m } } ^ { 2 } / { \mathrm { s } } ^ { 2 } } } = 1 4 5 ~ { \mathrm { m } } / { \mathrm { s } } .
$$

# Discussion

$1 4 5 ~ \mathsf { m / s }$ is about $5 2 2 ~ \mathrm { k m / h }$ or about $3 2 4 \mathrm { m i } / \mathrm { h }$ , but even this breakneck speed is short of the record for the quarter mile. Also, note that a square root has two values; we took the positive value to indicate a velocity in the same direction as the acceleration.

An examination of the equation $v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } )$ can produce further insights into the general relationships among physical quantities:

• The final velocity depends on how large the acceleration is and the distance over which it acts • For a fixed deceleration, a car that is going twice as fast doesn’t simply stop in twice the distance—it takes much further to stop. (This is why we have reduced speed zones near schools.)

# Putting Equations Together

In the following examples, we further explore one-dimensional motion, but in situations requiring slightly more algebraic manipulation. The examples also give insight into problem-solving techniques. The box below provides easy reference to the equations needed.

# EXAMPLE 2.12

# Calculating Displacement: How Far Does a Car Go When Coming to a Halt?

On dry concrete, a car can decelerate at a rate of $7 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ , whereas on wet concrete it can decelerate at only $5 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ . Find the distances necessary to stop a car moving at $3 0 . 0 ~ \mathsf { m } / \mathsf { s }$ (about $1 1 0 \mathsf { k m / h } )$ (a) on dry concrete and (b) on wet concrete. (c) Repeat both calculations, finding the displacement from the point where the driver sees a traffic light turn red, taking into account his reaction time of 0.500 s to get his foot on the brake.

# Strategy

Draw a sketch.

In order to determine which equations are best to use, we need to list all of the known values and identify exactly what we need to solve for. We shall do this explicitly in the next several examples, using tables to set them off.

# Solution for (a)

1. Identify the knowns and what we want to solve for. We know that $v _ { 0 } = 3 0 . 0 \mathrm { m / s }$ ; $v = 0$ ; $a = - 7 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ ( $a$ is negative because it is in a direction opposite to velocity). We take $x _ { 0 }$ to be 0. We are looking for displacement $\Delta x$ , or $x - x _ { 0 }$ .

2. Identify the equation that will help up solve the problem. The best equation to use is

$$
v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } ) .
$$

This equation is best because it includes only one unknown, $x$ . We know the values of all the other variables in this equation. (There are other equations that would allow us to solve for $x$ , but they require us to know the stopping time, $t$ , which we do not know. We could use them but it would entail additional calculations.)

3. Rearrange the equation to solve for $x$ .

$$
x - x _ { 0 } = \frac { v ^ { 2 } - v _ { 0 } ^ { 2 } } { 2 a }
$$

4. Enter known values.

$$
x - 0 = { \frac { 0 ^ { 2 } - ( 3 0 . 0 { \mathrm { m / s } } ) ^ { 2 } } { 2 \left( - 7 . 0 0 { \mathrm { m / s } } ^ { 2 } \right) } }
$$

Thus,

# Solution for (b)

This part can be solved in exactly the same manner as Part A. The only difference is that the deceleration is $- 5 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ . The result is

# Solution for (c)

Once the driver reacts, the stopping distance is the same as it is in Parts A and B for dry and wet concrete. So to answer this question, we need to calculate how far the car travels during the reaction time, and then add that to the stopping time. It is reasonable to assume that the velocity remains constant during the driver’s reaction time.

1. Identify the knowns and what we want to solve for. We know that $\overline { { v } } = 3 0 . 0 \mathrm { m / s }$ ; treaction $= 0 . 5 0 0 \mathrm { s }$ ; $a _ { \mathrm { r e a c t i o n } } = 0$   
We take $x _ { 0 - }$ to be 0. We are looking for .

2. Identify the best equation to use.

$x = x _ { 0 } + \overline { { v } } t$ works well because the only unknown value is $x$ , which is what we want to solve for.

3. Plug in the knowns to solve the equation.

$$
x = 0 + ( 3 0 . 0 \mathrm { m / s } ) ( 0 . 5 0 0 \mathrm { s } ) = 1 5 . 0 \mathrm { m } .
$$

This means the car travels ${ \displaystyle 1 5 . 0 ~ } \mathsf { m }$ while the driver reacts, making the total displacements in the two cases of dry and wet concrete ${ \displaystyle 1 5 . 0 ~ } \mathsf { m }$ greater than if he reacted instantly.

4. Add the displacement during the reaction time to the displacement when braking.

$$
x _ { \mathrm { b r a k i n g } } + x _ { \mathrm { r e a c t i o n } } = x _ { \mathrm { t o t a l } }
$$

a. $6 4 . 3 ~ \mathrm { m } + 1 5 . 0 ~ \mathrm { m } = 7 9 . 3 ~ \mathrm { m }$ when dry b. $9 0 . 0 \ : \mathrm { m } + 1 5 . 0 \ : \mathrm { m } = 1 0 5 \ : \mathrm { m }$ when wet

# Discussion

The displacements found in this example seem reasonable for stopping a fast-moving car. It should take longer to stop a car on wet rather than dry pavement. It is interesting that reaction time adds significantly to the displacements. But more important is the general approach to solving problems. We identify the knowns and the quantities to be determined and then find an appropriate equation. There is often more than one way to solve a problem. The various parts of this example can in fact be solved by other methods, but the solutions presented above are the shortest.

# EXAMPLE 2.13

# Calculating Time: A Car Merges into Traffic

Suppose a car merges into freeway traffic on a $2 0 0 - 1 1 0$ -long ramp. If its initial velocity is $1 0 . 0 ~ \mathsf { m } / \mathsf { s }$ and it accelerates at $2 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ , how long does it take to travel the $2 0 0 \mathrm { m }$ up the ramp? (Such information might be useful to a traffic engineer.)

# Strategy

Draw a sketch.

We are asked to solve for the time . As before, we identify the known quantities in order to choose a convenient physical relationship (that is, an equation with one unknown, $t )$ .

# Solution

1. Identify the knowns and what we want to solve for. We know that $v _ { \mathrm { 0 } } = 1 0 \mathrm { m / s }$ ; $a = 2 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ ; and $x = 2 0 0 \mathrm { m }$ . 2. We need to solve for . Choose the best equation. $\begin{array} { r } { x = x _ { 0 } + v _ { 0 } t + \frac { 1 } { 2 } a t ^ { 2 } } \end{array}$ works best because the only unknown in the equation is the variable $t$ for which we need to solve.

3. We will need to rearrange the equation to solve for $t$ . In this case, it will be easier to plug in the knowns first.

$$
2 0 0 \mathrm { m } = 0 \mathrm { m } + ( 1 0 . 0 \mathrm { m } / \mathrm { s } ) t + { \frac { 1 } { 2 } } \left( 2 . 0 0 \mathrm { m } / \mathrm { s } ^ { 2 } \right) t ^ { 2 }
$$

4. Simplify the equation. The units of meters $( \mathsf { m } )$ cancel because they are in each term. We can get the units of seconds (s) to cancel by taking $t = t \mathrm { ~ s ~ }$ , where $t$ is the magnitude of time and s is the unit. Doing so leaves

$$
2 0 0 = 1 0 t + t ^ { 2 } .
$$

5. Use the quadratic formula to solve for $t$ .

(a) Rearrange the equation to get 0 on one side of the equation.

$$
t ^ { 2 } + 1 0 t - 2 0 0 = 0
$$

This is a quadratic equation of the form

$$
a t ^ { 2 } + b t + c = 0 ,
$$

where the constants are $a = 1 . 0 0$ ， $b = 1 0 . 0$ ,and $c = - 2 0 0$ .

(b) Its solutions are given by the quadratic formula:

$$
t = { \frac { - b \pm { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } } .
$$

This yields two solutions for $t$ , which are

$$
t = 1 0 . 0 \ \mathrm { a n d } - 2 0 . 0 .
$$

In this case, then, the time is $t = t$ in seconds, or

$$
t = 1 0 . 0 \mathrm { ~ s ~ a n d } - 2 0 . 0 \mathrm { ~ s } .
$$

A negative value for time is unreasonable, since it would mean that the event happened 20 s before the motion began. We can discard that solution. Thus,

$$
t = 1 0 . 0 \mathrm { s } .
$$

# Discussion

Whenever an equation contains an unknown squared, there will be two solutions. In some problems both solutions are meaningful, but in others, such as the above, only one solution is reasonable. The 10.0 s answer seems reasonable for a typical freeway on-ramp.



With the basics of kinematics established, we can go on to many other interesting examples and applications. In the process of developing kinematics, we have also glimpsed a general approach to problem solving that produces both correct answers and insights into physical relationships. Problem-Solving Basics discusses problem-solving basics and outlines an approach that will help you succeed in this invaluable task.

# Making Connections: Take-Home Experiment—Breaking News

We have been using SI units of meters per second squared to describe some examples of acceleration or deceleration of cars, runners, and trains. To achieve a better feel for these numbers, one can measure the braking deceleration of a car doing a slow (and safe) stop. Recall that, for average acceleration, $\overline { { a } } = \Delta v / \Delta t$ . While traveling in a car, slowly apply the brakes as you come up to a stop sign. Have a passenger note the initial speed in miles per hour and the time taken (in seconds) to stop. From this, calculate the deceleration in miles per hour per second. Convert this to meters per second squared and compare with other decelerations mentioned in this chapter. Calculate the distance traveled in braking.

# CHECK YOUR UNDERSTANDING

A rocket accelerates at a rate of $2 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ during launch. How long does it take the rocket to reach a velocity of 400 m/s?

# Solution

To answer this, choose an equation that allows you to solve for time $t$ , given only $a$ , $v _ { 0 }$ , and $v$ .

$$
v = v _ { 0 } + a t
$$

Rearrange to solve for $t$ .

$$
t = { \frac { v - v _ { 0 } } { a } } = { \frac { 4 0 0 \mathrm { m / s } - 0 \mathrm { m / s } } { 2 0 \mathrm { m / s } ^ { 2 } } } = 2 0 \mathrm { s }
$$