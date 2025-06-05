# 3.4 Projectile Motion

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Identify and explain the properties of a projectile, such as acceleration due to gravity, range, maximum height, and trajectory. • Determine the location and velocity of a projectile at different points in its trajectory. • Apply the principle of independence of motion to solve projectile motion problems.

Projectile motion is the motion of an object thrown or projected into the air, subject to only the acceleration of gravity. The object is called a projectile, and its path is called its trajectory. The motion of falling objects, as covered in Problem-Solving Basics for One-Dimensional Kinematics, is a simple one-dimensional type of projectile motion in which there is no horizontal movement. In this section, we consider two-dimensional projectile motion, such as that of a football or other object for which air resistance isnegligible.

The most important fact to remember here is that motionsalongperpendicularaxesareindependentand thus can be analyzed separately. This fact was discussed in Kinematics in Two Dimensions: An Introduction, where vertical and horizontal motions were seen to be independent. The key to analyzing two-dimensional projectile motion is to break it into two motions, one along the horizontal axis and the other along the vertical. (This choice of axes is the most sensible, because acceleration due to gravity is vertical—thus, there will be no acceleration along the horizontal axis when air resistance is negligible.) As is customary, we call the horizontal axis the $x$ -axis and the vertical axis the y-axis. Figure 3.34 illustrates the notation for displacement, where is defined to be the total displacement and $\mathbf { x }$ and are its components along the horizontal and vertical axes, respectively. The magnitudes of these vectors are s, $x ,$ , and $y .$ (Note that in the last section we used the notation to represent a vector with components $\mathbf { A } _ { x }$ and $\mathbf { A } _ { y }$ . If we continued this format, we would call displacement with components $\mathbf { s } _ { x }$ and ${ \bf s } _ { y }$ . However, to simplify the notation, we will simply represent the component vectors as and .)

Of course, to describe motion we must deal with velocity and acceleration, as well as with displacement. We must find their components along the $x -$ and y-axes, too. We will assume all forces except gravity (such as air resistance and friction, for example) are negligible. The components of acceleration are then very simple: $a _ { y } = - g = - 9 . 8 0 \mathrm { m } / \mathrm { s } ^ { 2 }$ . (Note that this definition assumes that the upwards direction is defined as the positive

direction. If you arrange the coordinate system instead such that the downwards direction is positive, then acceleration due to gravity takes a positive value.) Because gravity is vertical, $a _ { x } = 0$ . Both accelerations are constant, so the kinematic equations can be used.

# Review of Kinematic Equations (constant )

$$
\begin{array} { l } { { \displaystyle x = x _ { 0 } + \overline { { v } } t } } \\ { { \displaystyle \overline { { v } } = \frac { v _ { 0 } + v } { 2 } } } \\ { { \displaystyle v = v _ { 0 } + a t } } \end{array}
$$

$$
x = x _ { 0 } + v _ { 0 } t + { \frac { 1 } { 2 } } a t ^ { 2 }
$$

$$
v ^ { 2 } = v _ { 0 } ^ { 2 } + 2 a ( x - x _ { 0 } ) .
$$

Given these assumptions, the following steps are then used to analyze projectile motion:

Step1.Resolveorbreakthemotionintohorizontalandverticalcomponentsalongthe $x -$ andy-axes.These axes are perpendicular, so $A _ { x } = A$ cos $\theta$ and $A _ { y } = A$ sin $\theta$ are used. The magnitude of the components of displacement along these axes are $x$ and $y .$ The magnitudes of the components of the velocity $\mathbf { v }$ are $v _ { x } = v$ cos $\theta$ and $v _ { y } = v$ where $v$ is the magnitude of the velocity and $\theta$ is its direction, as shown in Figure 3.35. Initial values are denoted with a subscript 0, as usual.

Step2.Treatthemotionastwoindependentone-dimensionalmotions,onehorizontalandtheothervertical. The kinematic equations for horizontal and vertical motion take the following forms:

Horizontal Motion $( a _ { x } = 0 )$ ） 3.33   
$x = x _ { 0 } + v _ { x } t$ 3.34   
$v _ { x } = v _ { 0 x } = v _ { x } =$ velocity is a constant. 3.35   
VerticalMotion   
(assuming positive is up 3.36   
$\begin{array} { c } { { a _ { y } = - g = - 9 . 8 0 \mathrm { m / s ^ { 2 } } ) } } \\ { { \ } } \\ { { y = y _ { 0 } + \displaystyle \frac { 1 } { 2 } ( v _ { 0 y } + v _ { y } ) t } } \\ { { \ v _ { y } = v _ { 0 y } - g t } } \\ { { \ } } \\ { { y = y _ { 0 } + v _ { 0 y } t - \displaystyle \frac { 1 } { 2 } g t ^ { 2 } } } \end{array}$ 3.37   
3.38   
3.39

$$
v _ { y } ^ { 2 } = v _ { 0 y } ^ { 2 } - 2 g ( y - y _ { 0 } ) .
$$

Step3.Solvefortheunknownsinthetwoseparatemotions—onehorizontalandonevertical. Note that the only common variable between the motions is time $t$ . The problem solving procedures here are the same as for onedimensional kinematics and are illustrated in the solved examples below.

Step4.Recombinethetwomotionstofindthetotaldisplacement andvelocity . Because the $x -$ and $y$ -motions are perpendicular, we determine these vectors by using the techniques outlined in the Vector Addition and Subtraction: Analytical Methods and employing $A = \sqrt { A _ { x } ^ { 2 } + A _ { y } ^ { 2 } }$ and $\theta = \tan ^ { - 1 } ( A _ { y } / A _ { x } )$ in the following form, where $\theta$ is the direction of the displacement and $\theta _ { v }$ is the direction of the velocity $\mathbf { v }$ :

Total displacement and velocity

$\begin{array} { r l r } & { } & { s = \sqrt { x ^ { 2 } + y ^ { 2 } } } \\ & { } & \\ & { } & { \theta = \tan ^ { - 1 } ( y / x ) } \\ & { } & { v = \sqrt { v _ { x } ^ { 2 } + v _ { y } ^ { 2 } } } \\ & { } & \\ & { } & { v = \tan ^ { - 1 } ( v _ { y } / v _ { x } } \end{array}$ 3.41   
3.42   
3.43   
3.44

# EXAMPLE 3.4

# A Fireworks Projectile Explodes High and Away

During a fireworks display, a shell is shot into the air with an initial speed of $7 0 . 0 \ : \mathrm { m } / \mathsf { s }$ at an angle of $7 5 . 0 ^ { \circ }$ above the horizontal, as illustrated in Figure 3.36. The fuse is timed to ignite the shell just as it reaches its highest point above the ground. (a) Calculate the height at which the shell explodes. (b) How much time passed between the launch of the shell and the explosion? (c) What is the horizontal displacement of the shell when it explodes?

# Strategy

Because air resistance is negligible for the unexploded shell, the analysis method outlined above can be used. The motion can be broken into horizontal and vertical motions in which $a _ { x } = 0$ and $a _ { y } = - g$ . We can then define $x _ { 0 }$ and $y _ { 0 }$ to be zero and solve for the desired quantities.

# Solution for (a)

By “height” we mean the altitude or vertical position $y$ above the starting point. The highest point in any trajectory, called the apex, is reached when $v _ { y } = 0$ . Since we know the initial and final velocities as well as the initial position, we use the following equation to find $y$ :

$$
v _ { y } ^ { 2 } = v _ { 0 y } ^ { 2 } - 2 g ( y - y _ { 0 } ) .
$$

Because $y _ { 0 }$ and $v _ { y }$ are both zero, the equation simplifies to

$$
0 = v _ { 0 y } ^ { 2 } - 2 g y .
$$

Solving for $y$ gives

$$
y = \frac { v _ { 0 y } ^ { 2 } } { 2 g } .
$$

Now we must find $v _ { 0 y }$ , the component of the initial velocity in the $y \cdot$ -direction. It is given by ${ { v } _ { 0 y } } = { { v } _ { 0 } }$ sin $\theta$ , where $v _ { 0 y }$ is the initial velocity of $7 0 . 0 \ : \mathrm { m } / \mathsf { s }$ , and $\theta _ { 0 } = 7 5 . 0 ^ { \circ }$ is the initial angle. Thus,

$$
v _ { 0 y } = v _ { 0 } \ \sin \theta _ { 0 } = ( 7 0 . 0 \mathrm { m / s } ) ( \sin 7 5 ^ { \circ } ) = 6 7 . 6 \ \mathrm { m / s } .
$$

and $y$ is

$$
y = { \frac { ( 6 7 . 6 \mathrm { m / s } ) ^ { 2 } } { 2 ( 9 . 8 0 \mathrm { m / s } ^ { 2 } ) } } ,
$$

so that

$$
y = 2 3 3 \mathrm { m } .
$$

# Discussion for (a)

Note that because up is positive, the initial velocity is positive, as is the maximum height, but the acceleration due to gravity is negative. Note also that the maximum height depends only on the vertical component of the initial velocity, so that any projectile with a $6 7 . 6 ~ \mathsf { m } / \mathsf { s }$ initial vertical component of velocity will reach a maximum height of $2 3 3 ~ \mathrm { m }$ (neglecting air resistance). The numbers in this example are reasonable for large fireworks displays, the shells of which do reach such heights before exploding. In practice, air resistance is not completely negligible, and so the initial velocity would have to be somewhat larger than that given to reach the same height.

# Solution for (b)

As in many physics problems, there is more than one way to solve for the time to the highest point. In this case, the easiest method is to use $\begin{array} { r } { y = y _ { 0 } + \frac { 1 } { 2 } ( v _ { 0 y } + v _ { y } ) t } \end{array}$ . Because $y _ { 0 }$ is zero, this equation reduces to simply

$$
y = \frac { 1 } { 2 } ( v _ { 0 y } + v _ { y } ) t .
$$

Note that the final vertical velocity, $v _ { y }$ , at the highest point is zero. Thus,

$$
\begin{array} { r c l } { t } & { = } & { \frac { 2 y } { ( v _ { 0 \mathrm { y } } + v _ { y } ) } = \frac { 2 ( 2 3 3 \mathrm { ~ m } ) } { ( 6 7 . 6 \mathrm { ~ m } / \mathrm { s } ) } } \\ & { = } & { 6 . 9 0 \mathrm { ~ s } . } \end{array}
$$

# Discussion for (b)

This time is also reasonable for large fireworks. When you are able to see the launch of fireworks, you will notice several seconds pass before the shell explodes. (Another way of finding the time is by using $\begin{array} { r } { y = y _ { 0 } + v _ { 0 y } t - \frac { 1 } { 2 } g t ^ { 2 } } \end{array}$ , and solving the quadratic equation for $t$ .)

# Solution for (c)

Because air resistance is negligible, $a _ { x } = 0$ and the horizontal velocity is constant, as discussed above. The horizontal displacement is horizontal velocity multiplied by time as given by $x = x _ { 0 } + v _ { x } t$ , where $x _ { 0 }$ is equal to zero:

$$
x = v _ { x } t ,
$$

where $\boldsymbol { v _ { x } }$ is the $x \cdot$ -component of the velocity, which is given by $v _ { x } = v _ { 0 }$ cos $\theta _ { 0 }$ Now,

$$
v _ { x } = v _ { 0 } \cos \theta _ { 0 } = ( 7 0 . 0 \mathrm { m / s } ) ( \cos 7 5 . 0 ^ { \circ } ) = 1 8 . 1 \mathrm { m / s } .
$$

The time $t$ for both motions is the same, and so $x$ is

$$
x = ( 1 8 . 1 \ \mathrm { m / s } ) ( 6 . 9 0 \ \mathrm { s } ) = 1 2 5 \ \mathrm { m } .
$$

# Discussion for (c)

The horizontal motion is a constant velocity in the absence of air resistance. The horizontal displacement found here could be useful in keeping the fireworks fragments from falling on spectators. Once the shell explodes, air resistance has a major effect, and many fragments will land directly below.

In solving part (a) of the preceding example, the expression we found for $y$ is valid for any projectile motion where air resistance is negligible. Call the maximum height $y = h$ ; then,

$$
h = \frac { v _ { 0 y } ^ { 2 } } { 2 g } .
$$

This equation defines the maximumheightofaprojectileand depends only on the vertical component of the initial velocity.

# Defining a Coordinate System

It is important to set up a coordinate system when analyzing projectile motion. One part of defining the coordinate system is to define an origin for the $x$ and $y$ positions. Often, it is convenient to choose the initial position of the object as the origin such that $x _ { 0 } = 0$ and $y _ { 0 } = 0$ . It is also important to define the positive and negative directions in the $x$ and $y$ directions. Typically, we define the positive vertical direction as upwards, and the positive horizontal direction is usually the direction of the object’s motion. When this is the case, the vertical acceleration, $g$ , takes a negative value (since it is directed downwards towards the Earth). However, it is occasionally useful to define the coordinates differently. For example, if you are analyzing the motion of a ball thrown downwards from the top of a cliff, it may make sense to define the positive direction downwards since the motion of the ball is solely in the downwards direction. If this is the case, $g$ takes a positive value.



# EXAMPLE 3.5

# Calculating Projectile Motion: Hot Rock Projectile

Kilauea in Hawaii is the world’s most continuously active volcano. Very active volcanoes characteristically eject redhot rocks and lava rather than smoke and ash. Suppose a large rock is ejected from the volcano with a speed of 25.0 $\mathsf { m } / \mathsf { s }$ and at an angle $3 5 . 0 ^ { \mathrm { o } }$ above the horizontal, as shown in Figure 3.37. The rock strikes the side of the volcano at an altitude $2 0 . 0 \mathsf { m }$ lower than its starting point. (a) Calculate the time it takes the rock to follow this path. (b) What are the magnitude and direction of the rock’s velocity at impact?

# Strategy

Again, resolving this two-dimensional motion into two independent one-dimensional motions will allow us to solve for the desired quantities. The time a projectile is in the air is governed by its vertical motion alone. We will solve for $t$ first. While the rock is rising and falling vertically, the horizontal motion continues at a constant velocity. This example asks for the final velocity. Thus, the vertical and horizontal results will be recombined to obtain $v$ and $\theta _ { v }$ at the final time determined in the first part of the example.

# Solution for (a)

While the rock is in the air, it rises and then falls to a final position $2 0 . 0 \mathrm { m }$ lower than its starting altitude. We can find the time for this by using

$$
y = y _ { 0 } + v _ { 0 y } t - { \frac { 1 } { 2 } } g t ^ { 2 } .
$$

If we take the initial position $y _ { 0 }$ to be zero, then the final position is $y = - 2 0 . 0 \mathrm { m }$ Now the initial vertical velocity is the vertical component of the initial velocity, found from $v _ { 0 y } = v _ { 0 }$ sin $\theta _ { 0 } = ( 2 5 . 0 \ \mathrm { m / s } ) ( \sin 3 5 . 0 ^ { \circ } ) = 1 4 . 3 \ \mathrm { m / s }$ . Substituting known values yields

$$
- 2 0 . 0 \mathrm { m } = ( 1 4 . 3 \mathrm { m } / \mathrm { s } ) t - \big ( 4 . 9 0 \mathrm { m } / \mathrm { s } ^ { 2 } \big ) t ^ { 2 } .
$$

Rearranging terms gives a quadratic equation in $t$ :

$$
\big ( 4 . 9 0 \mathrm { m } / \mathrm { s } ^ { 2 } \big ) t ^ { 2 } - ( 1 4 . 3 \mathrm { m } / \mathrm { s } ) t - ( 2 0 . 0 \mathrm { m } ) = 0 .
$$

This expression is a quadratic equation of the form $a t ^ { 2 } + b t + c = 0$ , where the constants are $a = 4 . 9 0 , b = - 1 4 . 3$ , and $c = - 2 0 . 0 \$ Its solutions are given by the quadratic formula:

$$
t = { \frac { - b \pm { \sqrt { b ^ { 2 } - 4 a c } } } { 2 a } } .
$$

This equation yields two solutions: $t = 3 . 9 6$ and $t = - 1 . 0 3$ . (It is left as an exercise for the reader to verify these

solutions.) The time is $t = 3 . 9 6 :$ or . The negative value of time implies an event before the start of motion, and so we discard it. Thus,

$$
t = 3 . 9 6 \mathrm { s } .
$$

# Discussion for (a)

The time for projectile motion is completely determined by the vertical motion. So any projectile that has an initial vertical velocity of $\mathtt { 1 4 . 3 } \mathsf { m } / \mathsf { s }$ and lands $2 0 . 0 \mathrm { m }$ below its starting altitude will spend 3.96 s in the air.

# Solution for (b)

From the information now in hand, we can find the final horizontal and vertical velocities $v _ { x }$ and $v _ { y }$ and combine them to find the total velocity $v$ and the angle $\theta _ { 0 }$ it makes with the horizontal. Of course, $\boldsymbol { v _ { x } }$ is constant so we can solve for it at any horizontal location. In this case, we chose the starting point since we know both the initial velocity and initial angle. Therefore:

$$
v _ { x } = v _ { 0 } \cos \theta _ { 0 } = ( 2 5 . 0 \mathrm { m / s } ) ( \cos 3 5 ^ { \circ } ) = 2 0 . 5 \mathrm { m / s } .
$$

The final vertical velocity is given by the following equation:

$$
v _ { y } = v _ { 0 y } - g t ,
$$

where $v _ { 0 \mathrm { y } }$ was found in part (a) to be $1 4 . 3 \mathrm { m / s }$ . Thus,

$$
v _ { y } = 1 4 . 3 ~ \mathrm { m / s } - ( 9 . 8 0 ~ \mathrm { m / s } ^ { 2 } ) ( 3 . 9 6 ~ \mathrm { s } )
$$

so that

$$
v _ { y } = - 2 4 . 5 \mathrm { m / s } .
$$

To find the magnitude of the final velocity $v$ we combine its perpendicular components, using the following equation:

$$
v = \sqrt { v _ { x } ^ { 2 } + v _ { y } ^ { 2 } } = \sqrt { ( 2 0 . 5 \mathrm { ~ m } / \mathrm { s } ) ^ { 2 } + ( - 2 4 . 5 \mathrm { ~ m } / \mathrm { s } ) ^ { 2 } } ,
$$

which gives

$$
v = 3 1 . 9 \mathrm { m / s } .
$$

The direction $\theta _ { v }$ is found from the equation:

$$
\theta _ { v } = \tan ^ { - 1 } ( v _ { y } / v _ { x } )
$$

so that

$$
\theta _ { v } = \tan ^ { - 1 } ( - 2 4 . 5 / 2 0 . 5 ) = \tan ^ { - 1 } ( - 1 . 1 9 ) .
$$

Thus,

$$
\theta _ { v } = - 5 0 . 1 ^ { \circ } .
$$

# Discussion for (b)

The negative angle means that the velocity is $5 0 . 1 ^ { \circ }$ below the horizontal. This result is consistent with the fact that the final vertical velocity is negative and hence downward—as you would expect because the final altitude is $2 0 . 0 \mathsf { m }$ lower than the initial altitude. (See Figure 3.37.)

One of the most important things illustrated by projectile motion is that vertical and horizontal motions are independent of each other. Galileo was the first person to fully comprehend this characteristic. He used it to predict the range of a projectile. On level ground, we define range to be the horizontal distance $R$ traveled by a projectile. Galileo and many others were interested in the range of projectiles primarily for military purposes—such as aiming cannons. However, investigating the range of projectiles can shed light on other interesting phenomena, such as the orbits of satellites around the Earth. Let us consider projectile range further.

How does the initial velocity of a projectile affect its range? Obviously, the greater the initial speed $v _ { 0 }$ , the greater the range, as shown in Figure 3.38(a). The initial angle $\theta _ { 0 }$ also has a dramatic effect on the range, as illustrated in Figure 3.38(b). For a fixed initial speed, such as might be produced by a cannon, the maximum range is obtained with $\theta _ { 0 } = 4 5 ^ { \mathrm { o } }$ . This is true only for conditions neglecting air resistance. If air resistance is considered, the maximum angle is approximately $3 8 ^ { \circ }$ . Interestingly, for every initial angle except $4 5 ^ { \circ }$ , there are two angles that give the same range—the sum of those angles is $9 0 ^ { \circ }$ . The range also depends on the value of the acceleration of gravity $g$ . The lunar astronaut Alan Shepherd was able to drive a golf ball a great distance on the Moon because gravity is weaker there. The range $R$ of a projectile on levelgroundfor which air resistance is negligible is given by

$$
R = \frac { v _ { 0 } ^ { 2 } \sin 2 \theta _ { 0 } } { g } ,
$$

where $v _ { 0 }$ is the initial speed and $\theta _ { 0 }$ is the initial angle relative to the horizontal. The proof of this equation is left as an end-of-chapter problem (hints are given), but it does fit the major features of projectile range as described.

When we speak of the range of a projectile on level ground, we assume that $R$ is very small compared with the circumference of the Earth. If, however, the range is large, the Earth curves away below the projectile and acceleration of gravity changes direction along the path. The range is larger than predicted by the range equation given above because the projectile has farther to fall than it would on level ground. (See Figure 3.39.) If the initial speed is great enough, the projectile goes into orbit. This possibility was recognized centuries before it could be accomplished. When an object is in orbit, the Earth curves away from underneath the object at the same rate as it falls. The object thus falls continuously but never hits the surface. These and other aspects of orbital motion, such as the rotation of the Earth, will be covered analytically and in greater depth later in this text.

Once again we see that thinking about one topic, such as the range of a projectile, can lead us to others, such as the Earth orbits. In Addition of Velocities, we will examine the addition of velocities, which is another important aspect of two-dimensional kinematics and will also yield insights beyond the immediate topic.

# PHET EXPLORATIONS

# Projectile Motion

Blast a Buick out of a cannon! Learn about projectile motion by firing various objects. Set the angle, initial speed, and mass. Add air resistance. Make a game out of this simulation by trying to hit a target.

Click to view content (https://openstax.org/books/college-physics-2e/pages/3-4-projectile-motion)