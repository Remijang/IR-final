# 16.2 Entropy

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

• Define entropy • Explain the relationship between entropy and the number of microstates • Predict the sign of the entropy change for chemical and physical processes

In 1824, at the age of 28, Nicolas Léonard Sadi Carnot (Figure 16.7) published the results of an extensive study regarding the efficiency of steam heat engines. A later review of Carnot’s findings by Rudolf Clausius introduced a new thermodynamic property that relates the spontaneous heat flow accompanying a process to the temperature at which the process takes place. This new property was expressed as the ratio of the reversibleheat $( q _ { \mathrm { r e v } } )$ and the kelvin temperature (T). In thermodynamics, a reversible process is one that takes place at such a slow rate that it is always at equilibrium and its direction can be changed (it can be “reversed”) by an infinitesimally small change in some condition. Note that the idea of a reversible process is a formalism required to support the development of various thermodynamic concepts; no real processes are truly reversible, rather they are classified as ir eversible.

Similar to other thermodynamic properties, this new quantity is a state function, so its change depends only upon the initial and final states of a system. In 1865, Clausius named this property entropy (S) and defined its change for any process as the following:

$$
\Delta S = { \frac { q _ { \mathrm { r e v } } } { T } }
$$

The entropy change for a real, irreversible process is then equal to that for the theoretical reversible process that involves the same initial and final states.

# Entropy and Microstates

Following the work of Carnot and Clausius, Ludwig Boltzmann developed a molecular-scale statistical model that related the entropy of a system to the numberofmicrostates(W) possible for the system. A microstate is a specific configuration of all the locations and energies of the atoms or molecules that make up a system. The relation between a system’s entropy and the number of possible microstates is

$$
S = k \ln W
$$

where $k$ is the Boltzmann constant, $1 . 3 8 \times 1 0 ^ { - 2 3 } \mathrm { J / K }$ .

As for other state functions, the change in entropy for a process is the difference between its final $( S _ { \mathrm { f } } )$ and initial $( S _ { \mathrm { i } } )$ values:

$$
\Delta S = S _ { \mathrm { f } } - S _ { \mathrm { i } } = k \ln W _ { \mathrm { f } } - k \ln W _ { \mathrm { i } } = k \ln { \frac { W _ { \mathrm { f } } } { W _ { \mathrm { i } } } }
$$

For processes involving an increase in the number of microstates, $W _ { \mathrm { f } } > W _ { \mathrm { i } }$ , the entropy of the system increases and $\Delta S > 0$ . Conversely, processes that reduce the number of microstates, $W _ { \mathrm { f } } < W _ { \mathrm { i } } ,$ , yield a decrease in system entropy, $\Delta S < 0$ . This molecular-scale interpretation of entropy provides a link to the probability that a process will occur as illustrated in the next paragraphs.

Consider the general case of a system comprised of $N$ particles distributed among $n$ boxes. The number of microstates possible for such a system is $n ^ { N } .$ . For example, distributing four particles among two boxes will result in $2 ^ { 4 } = 1 6$ different microstates as illustrated in Figure 16.8. Microstates with equivalent particle arrangements (not considering individual particle identities) are grouped together and are called distributions. The probability that a system will exist with its components in a given distribution is proportional to the number of microstates within the distribution. Since entropy increases logarithmically with the number of microstates, themostprobabledistributionisthereforetheoneofgreatestentropy.

For this system, the most probable configuration is one of the six microstates associated with distribution (c) where the particles are evenly distributed between the boxes, that is, a configuration of two particles in each box. The probability of finding the system in this configuration is $\frac { 6 } { 1 6 }$ or $\frac { 3 } { 8 }$ The least probable configuration of the system is one in which all four particles are in one box, corresponding to distributions (a) and (e), each with a probability of $\textstyle { \frac { 1 } { 1 6 } }$ The probability of finding all particles in only one box (either the left box or right box) is then $\begin{array} { r } { \left( \frac { 1 } { 1 6 } + \frac { 1 } { 1 6 } \right) = \frac { 2 } { 1 6 } \operatorname { o r } \frac { 1 } { 8 } } \end{array}$



As you add more particles to the system, the number of possible microstates increases exponentially $( 2 ^ { N } )$ . A macroscopic (laboratory-sized) system would typically consist of moles of particles $( N \sim 1 0 ^ { 2 3 } )$ , and the corresponding number of microstates would be staggeringly huge. Regardless of the number of particles in the system, however, the distributions in which roughly equal numbers of particles are found in each box are always the most probable configurations.

This matter dispersal model of entropy is often described qualitatively in terms of the disorderof the system. By this description, microstates in which all the particles are in a single box are the most ordered, thus possessing the least entropy. Microstates in which the particles are more evenly distributed among the boxes are more disordered, possessing greater entropy.

The previous description of an ideal gas expanding into a vacuum (Figure 16.4) is a macroscopic example of this particle-in-a-box model. For this system, the most probable distribution is confirmed to be the one in which the matter is most uniformly dispersed or distributed between the two flasks. Initially, the gas molecules are confined to just one of the two flasks. Opening the valve between the flasks increases the volume available to the gas molecules and, correspondingly, the number of microstates possible for the system. Since $W _ { \mathrm { f } } > W _ { \mathrm { i } }$ , the expansion process involves an increase in entropy $( \Delta S > 0 )$ and is spontaneous.

A similar approach may be used to describe the spontaneous flow of heat. Consider a system consisting of two objects, each containing two particles, and two units of thermal energy (represented as “\*”) in Figure 16.9. The hot object is comprised of particles A and B and initially contains both energy units. The cold object is comprised of particles C and D, which initially has no energy units. Distribution (a) shows the three microstates possible for the initial state of the system, with both units of energy contained within the hot object. If one of the two energy units is transferred, the result is distribution (b) consisting of four microstates. If both energy units are transferred, the result is distribution (c) consisting of three microstates. Thus, we may describe this system by a total of ten microstates. The probability that the heat does not flow when the two objects are brought into contact, that is, that the system remains in distribution (a), is $\textstyle { \frac { 3 } { 1 0 } }$ More likely is the flow of heat to yield one of the other two distribution, the combined probability being $\frac { 7 } { 1 0 }$ The most likely result is the flow of heat to yield the uniform dispersal of energy represented by distribution (b), the probability of this configuration being $\frac { 4 } { 1 0 }$ This supports the common observation that placing hot and cold objects in contact results in spontaneous heat flow that ultimately equalizes the objects’ temperatures. And, again, this spontaneous process is also characterized by an increase in system entropy.

# EXAMPLE 16.2

# Determination of ΔS

Calculate the change in entropy for the process depicted below.

# Solution

The initial number of microstates is one, the final six:

$$
\Delta S = k \ln { \frac { W _ { \mathrm { c } } } { W _ { \mathrm { a } } } } = 1 . 3 8 \times 1 0 ^ { - 2 3 } { \mathrm { J / K } } \times \ln { \frac { 6 } { 1 } } = 2 . 4 7 \times 1 0 ^ { - 2 3 } { \mathrm { J / K } }
$$

The sign of this result is consistent with expectation; since there are more microstates possible for the final state than for the initial state, the change in entropy should be positive.

# Check Your Learning

Consider the system shown in Figure 16.9. What is the change in entropy for the process where al the energy is transferred from the hot object (AB) to the cold object (CD)?

# Predicting the Sign of ΔS

The relationships between entropy, microstates, and matter/energy dispersal described previously allow us to make generalizations regarding the relative entropies of substances and to predict the sign of entropy changes for chemical and physical processes. Consider the phase changes illustrated in Figure 16.10. In the solid phase, the atoms or molecules are restricted to nearly fixed positions with respect to each other and are capable of only modest oscillations about these positions. With essentially fixed locations for the system’s component particles, the number of microstates is relatively small. In the liquid phase, the atoms or molecules are free to move over and around each other, though they remain in relatively close proximity to one another. This increased freedom of motion results in a greater variation in possible particle locations, so the number of microstates is correspondingly greater than for the solid. As a result, $S _ { \mathrm { l i q u i d } } > S _ { \mathrm { s o l i d } }$ and the process of converting a substance from solid to liquid (melting) is characterized by an increase in entropy, $\Delta S > 0$ . By the same logic, the reciprocal process (freezing) exhibits a decrease in entropy, $\Delta S < 0$ .

Now consider the gaseous phase, in which a given number of atoms or molecules occupy a muchgreater volume than in the liquid phase. Each atom or molecule can be found in many more locations, corresponding to a much greater number of microstates. Consequently, for any substance, $S _ { \mathrm { g a s } } > S _ { \mathrm { l i q u i d } } > S _ { \mathrm { s o l i d } }$ , and the processes of vaporization and sublimation likewise involve increases in entropy, $\Delta S > 0$ . Likewise, the reciprocal phase transitions, condensation and deposition, involve decreases in entropy, $\Delta S < 0$ .

According to kinetic-molecular theory, the temperature of a substance is proportional to the average kinetic energy of its particles. Raising the temperature of a substance will result in more extensive vibrations of the particles in solids and more rapid translations of the particles in liquids and gases. At higher temperatures, the distribution of kinetic energies among the atoms or molecules of the substance is also broader (more dispersed) than at lower temperatures. Thus, the entropy for any substance increases with temperature (Figure 16.11).

# LINK TO LEARNING

Try this simulator (http://openstax.org/l/16freemotion) with interactive visualization of the dependence of particle location and freedom of motion on physical state and temperature.



The entropy of a substance is influenced by the structure of the particles (atoms or molecules) that comprise the substance. With regard to atomic substances, heavier atoms possess greater entropy at a given temperature than lighter atoms, which is a consequence of the relation between a particle’s mass and the spacing of quantized translational energy levels (a topic beyond the scope of this text). For molecules, greater numbers of atoms increase the number of ways in which the molecules can vibrate and thus the number of possible microstates and the entropy of the system.

Finally, variations in the types of particles affects the entropy of a system. Compared to a pure substance, in which all particles are identical, the entropy of a mixture of two or more different particle types is greater. This is because of the additional orientations and interactions that are possible in a system comprised of nonidentical components. For example, when a solid dissolves in a liquid, the particles of the solid experience both a greater freedom of motion and additional interactions with the solvent particles. This corresponds to a more uniform dispersal of matter and energy and a greater number of microstates. The process of dissolution therefore involves an increase in entropy, $\Delta S > 0$ .

Considering the various factors that affect entropy allows us to make informed predictions of the sign of $\Delta S$ for various chemical and physical processes as illustrated in Example 16.3.

# EXAMPLE 16.3

# Predicting the Sign of ∆S

Predict the sign of the entropy change for the following processes. Indicate the reason for each of your predictions.

(a) One mole liquid water at room temperature $\longrightarrow$ one mole liquid water at $5 0 ^ { \circ } \mathrm { C }$   
(b) $\mathrm { A g } ^ { + } ( a q ) + \mathrm { C l } ^ { - } ( a q ) \longrightarrow \mathrm { A g C l } ( s )$   
(c) $\begin{array} { r } { \mathrm { C } _ { 6 } \mathrm { H } _ { 6 } ( l ) + \frac { 1 5 } { 2 } \mathrm { O } _ { 2 } ( g ) \longrightarrow 6 \mathrm { C O } _ { 2 } ( g ) + 3 \mathrm { H } _ { 2 } \mathrm { O } ( l ) } \end{array}$   
(d) $\mathrm { N H } _ { 3 } ( s ) \longrightarrow \mathrm { N H } _ { 3 } ( l )$

# Solution

(a) positive, temperature increases   
(b) negative, reduction in the number of ions (particles) in solution, decreased dispersal of matter   
(c) negative, net decrease in the amount of gaseous species   
(d) positive, phase transition from solid to liquid, net increase in dispersal of matter

# Check Your Learning

Predict the sign of the entropy change for the following processes. Give a reason for your prediction.

(a) $\mathrm { N a N O } _ { 3 } ( s ) \longrightarrow \mathrm { N a } ^ { + } ( a q ) + \mathrm { N O } _ { 3 } { } ^ { - } ( a q )$ (b) the freezing of liquid water (c) $\mathrm { C O } _ { 2 } ( s ) \longrightarrow \mathrm { C O } _ { 2 } ( g )$ (d) $\mathrm { C a C O } _ { 3 } ( s ) \longrightarrow \mathrm { C a O } ( s ) + \mathrm { C O } _ { 2 } ( g )$

# Answer:

(a) Positive; The solid dissolves to give an increase of mobile ions in solution. (b) Negative; The liquid becomes a more ordered solid. (c) Positive; The relatively ordered solid becomes a gas. (d) Positive; There is a net increase in the amount of gaseous species.