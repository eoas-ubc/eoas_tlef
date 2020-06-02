## EOSC 211: Some Numerical Integration - Assignment 2 background

**Movies**

Sketch how you think the spacecraft’s flight path and speeds in the two
other trajectories will compare with the one shown.

**Sketching out the Problem:**

**1.** sketch the direction of the force and acceleration on the
spacecraft in A.

2\. sketch the spacecraft’s position, velocity and acceleration at some
time t = ∆t later in B.

**Calculations**:

We will use the initial conditions from Part 5 of the assignment:

s<sub>x0</sub> = -3050 km

s<sub>y0</sub> = -3 \* R<sub>merc</sub>

v<sub>y0</sub> = 7 km/s in the positive y-direction

v<sub>x0</sub> = 0

The values for the mass and radius of Mercury and the gravitational
constant, G, are

M<sub>merc</sub> = 3.3 x10<sup>23</sup> kg

R<sub>merc</sub> = 2440 km

G = 6.67 x10<sup>-11</sup> m<sup>3</sup> kg<sup>-1</sup> s<sup>-2</sup>

**Step 1:** Fill in the initial conditions – ie the x-y coordinates of
speed and position of the spacecraft at time t=0 in cols 5-8 of row 1 of
the table. Calculate, s the distance of the spacecraft from the planet,
and s<sup>2</sup>.

<table>
<thead>
<tr class="header">
<th><strong>t (s)</strong></th>
<th><strong>∆v<sub>x</sub> (m/s)</strong></th>
<th><strong>∆v<sub>y</sub> (m/s)</strong></th>
<th><strong>∆s<sub>x</sub> (m)</strong></th>
<th><strong>∆s<sub>y</sub> (m)</strong></th>
<th><strong>v<sub>x</sub> (m/s)</strong></th>
<th><strong>v<sub>y</sub> (m/s)</strong></th>
<th><p><strong>s<sub>x</sub></strong></p>
<p><strong>(m)</strong></p></th>
<th><p><strong>s<sub>y</sub></strong></p>
<p><strong>(m)</strong></p></th>
<th><strong>s<sup>2</sup> (m)</strong></th>
<th><strong>a (m/s<sup>2</sup>)</strong></th>
<th><strong>a<sub>x</sub> (m/s<sup>2</sup>)</strong></th>
<th><strong>a<sub>y</sub> (m/s<sup>2</sup>)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>0</strong></td>
<td><strong>XXX</strong></td>
<td><strong>XXX</strong></td>
<td><strong>XXX</strong></td>
<td><strong>XXX</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>60</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>120</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

**Step 2:** Calculate the magnitude of the acceleration, a, on the
spacecraft at time, t=0 due to the planet and add it to the table above.
Resolve the acceleration into its x- and y- coordinates and fill these
in (a<sub>x</sub> and a<sub>y</sub>).

**Step 3:** If we assume the acceleration is constant over a time
interval ∆t, then after the time ∆t there is a change in velocity due to
this acceleration. This is in the direction of the acceleration vector
so the easiest thing is to work in terms of the x- and y- components of
the change in velocity.

> Write down the equations for the x- and y- components of the *change
> in velocity* in terms of the x- and y- components of acceleration and
> the time interval ∆t.

∆v<sub>x</sub> = \_\_\_\_\_\_\_\_\_\_\_ ∆v<sub>y</sub> =
\_\_\_\_\_\_\_\_\_\_\_

> Similarly there is a change in position, which depends both on the
> velocity at the beginning of the time interval and on the
> acceleration:
> 
> ∆s<sub>x</sub> = v<sub>x</sub> ∆t + ½ a<sub>x</sub> ∆t<sup>2</sup>
> ∆s<sub>y</sub> = v<sub>y</sub> ∆t + ½ a<sub>y</sub> ∆t<sup>2</sup>
> 
> Fill in these changes in velocity and position (occurring after 60
> seconds) in row 2, columns 1-4 of the table.

**Step 4:** The new velocity after a time ∆t is the initial velocity
plus the change in velocity.

> So in our table above we can calculate the x- and y-components of
> velocity at t=60 seconds using

v<sub>x</sub><sup>t=60</sup> = v<sub>x</sub><sup>t=0</sup> +
∆v<sub>x</sub> v<sub>y</sub><sup>t=60</sup> =
v<sub>y</sub><sup>t=0</sup> + ∆v<sub>y</sub>

> and the x- and y- components of position at t= 60 seconds using
> 
> s<sub>x</sub><sup>t=60</sup> = s<sub>x</sub><sup>t=0</sup> +
> ∆s<sub>x</sub> s<sub>y</sub><sup>t=60</sup> =
> s<sub>y</sub><sup>t=0</sup> + ∆s<sub>y</sub>
> 
> Calculate the new v<sub>x</sub>, v<sub>y</sub>, s<sub>x</sub>,
> s<sub>y</sub> and fill in columns 5-8 of the second row of the table.

**Step 5:** You can now see that you can essentially repeat steps 2-4
for each successive 60 seconds of the spacecraft’s trajectory using
Steps 2-4 above. To calculate the entire spacecraft trajectory you would
repeat steps 2-4 until you have reached a time t = t<sub>final</sub>
(given as 40 minutes in part 5 of the assignment). **Hint:** If you do
this by hand (correctly\!) for the first 3 rows given you can of course
check your MATLAB code using this table….
