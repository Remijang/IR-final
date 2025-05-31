# 17.7 Ultrasound

# LEARNING OBJECTIVES

By the end of this section, you will be able to:

Define acoustic impedance and intensity reflection coefficient. • Describe medical and other uses of ultrasound technology. • Calculate acoustic impedance using density values and the speed of ultrasound. • Calculate the velocity of a moving object using Doppler-shifted ultrasound.

Any sound with a frequency above $2 0 , 0 0 0 \mathsf { H z }$ (or $2 0 \mathsf { k H z } ,$ )—that is, above the highest audible frequency—is defined to be ultrasound. In practice, it is possible to create ultrasound frequencies up to more than a gigahertz. (Higher frequencies are difficult to create; furthermore, they propagate poorly because they are very strongly absorbed.) Ultrasound has a tremendous number of applications, which range from burglar alarms to use in cleaning delicate objects to the guidance systems of bats. We begin our discussion of ultrasound with some of its applications in medicine, in which it is used extensively both for diagnosis and for therapy.

# Characteristics of Ultrasound

The characteristics of ultrasound, such as frequency and intensity, are wave properties common to all types of waves. Ultrasound also has a wavelength that limits the fineness of detail it can detect. This characteristic is true of all waves. We can never observe details significantly smaller than the wavelength of our probe; for example, we will never see individual atoms with visible light, because the atoms are so small compared with the wavelength of light.

# Ultrasound in Medical Therapy

Ultrasound, like any wave, carries energy that can be absorbed by the medium carrying it, producing effects that vary with intensity. When focused to intensities of $1 0 ^ { 3 }$ to $1 0 ^ { 5 } \mathrm { W } / \mathrm { m } ^ { 2 }$ , ultrasound can be used to shatter gallstones or pulverize cancerous tissue in surgical procedures. (See Figure 17.41.) Intensities this great can damage individual cells, variously causing their protoplasm to stream inside them, altering their permeability, or rupturing their walls through cavitation. Cavitation is the creation of vapor cavities in a fluid—the longitudinal vibrations in ultrasound alternatively compress and expand the medium, and at sufficient amplitudes the expansion separates molecules. Most cavitation damage is done when the cavities collapse, producing even greater shock pressures.

Most of the energy carried by high-intensity ultrasound in tissue is converted to thermal energy. In fact, intensities of $1 0 ^ { 3 }$ to $1 0 ^ { 4 } \mathrm { W } / \mathrm { m } ^ { 2 }$ are commonly used for deep-heat treatments called ultrasound diathermy. Frequencies of 0.8 to $\mathsf { 1 } \mathsf { M } \mathsf { H } z$ are typical. In both athletics and physical therapy, ultrasound diathermy is most often applied to injured or overworked muscles to relieve pain and improve flexibility. Skill is needed by the therapist to avoid “bone burns” and other tissue damage caused by overheating and cavitation, sometimes made worse by reflection and focusing of the ultrasound by joint and bone tissue.

In some instances, you may encounter a different decibel scale, called the sound pres urelevel, when ultrasound travels in water or in human and other biological tissues. We shall not use the scale here, but it is notable that numbers for sound pressure levels range 60 to 70 dB higher than you would quote for $\beta$ , the sound intensity level used in this text. Should you encounter a sound pressure level of 220 decibels, then, it is not an astronomically high intensity, but equivalent to about 155 dB—high enough to destroy tissue, but not as unreasonably high as it might seem at first.

# Ultrasound in Medical Diagnostics

When used for imaging, ultrasonic waves are emitted from a transducer, a crystal exhibiting the piezoelectric effect (the expansion and contraction of a substance when a voltage is applied across it, causing a vibration of the crystal). These high-frequency vibrations are transmitted into any tissue in contact with the transducer. Similarly, if a pressure is applied to the crystal (in the form of a wave reflected off tissue layers), a voltage is produced which can be recorded. The crystal therefore acts as both a transmitter and a receiver of sound. Ultrasound is also partially absorbed by tissue on its path, both on its journey away from the transducer and on its return journey. From the time between when the original signal is sent and when the reflections from various boundaries between media are received, (as well as a measure of the intensity loss of the signal), the nature and position of each boundary between tissues and organs may be deduced.

Reflections at boundaries between two different media occur because of differences in a characteristic known as the acoustic impedance $Z$ of each substance. Impedance is defined as

$$
Z = \rho v ,
$$

where $\rho$ is the density of the medium (in $\mathrm { k g / m } ^ { 3 }$ ) and $v$ is the speed of sound through the medium (in ${ \mathfrak { m } } / { \mathfrak { s } } ,$ ). The units for $Z$ are therefore $\mathrm { k g } / ( \mathrm { m } ^ { 2 } \cdot \mathrm { s } )$ .

Table 17.5 shows the density and speed of sound through various media (including various soft tissues) and the associated acoustic impedances. Note that the acoustic impedances for soft tissue do not vary much but that there is a big difference between the acoustic impedance of soft tissue and air and also between soft tissue and bone.

At the boundary between media of different acoustic impedances, some of the wave energy is reflected and some is transmitted. The greater the diferencein acoustic impedance between the two media, the greater the reflection and the smaller the transmission.

The intensity reflection coefficient $a$ is defined as the ratio of the intensity of the reflected wave relative to the incident (transmitted) wave. This statement can be written mathematically as

$$
a = \frac { ( Z _ { 2 } - Z _ { 1 } ) ^ { 2 } } { ( Z _ { 1 } + Z _ { 2 } ) ^ { 2 } } ,
$$

where $Z _ { 1 }$ and $Z _ { 2 }$ are the acoustic impedances of the two media making up the boundary. A reflection coefficient of zero (corresponding to total transmission and no reflection) occurs when the acoustic impedances of the two media are the same. An impedance “match” (no reflection) provides an efficient coupling of sound energy from one medium to another. The image formed in an ultrasound is made by tracking reflections (as shown in Figure 17.42) and mapping the intensity of the reflected sound waves in a two-dimensional plane.

# EXAMPLE 17.7

# Calculate Acoustic Impedance and Intensity Reflection Coefficient: Ultrasound and Fat Tissue

(a) Using the values for density and the speed of ultrasound given in Table 17.5, show that the acoustic impedance of fat tissue is indeed $1 . 3 4 \times 1 0 ^ { 6 } \mathrm { k g } / ( \mathrm { m } ^ { 2 } { \cdot } \mathrm { s } )$ .

(b) Calculate the intensity reflection coefficient of ultrasound when going from fat to muscle tissue.

# Strategy for (a)

The acoustic impedance can be calculated using $Z = \rho v$ and the values for $\rho$ and $v$ found in Table 17.5.

# Solution for (a)

(1) Substitute known values from Table 17.5 into $Z = \rho v$ .

$$
Z = \rho v = \left( 9 2 5 \mathrm { k g / m } ^ { 3 } \right) ( 1 4 5 0 \mathrm { m / s } )
$$

(2) Calculate to find the acoustic impedance of fat tissue.

$$
1 . 3 4 \times 1 0 ^ { 6 } \mathrm { k g } / ( \mathrm { m } ^ { 2 } { \cdot } \mathrm { s } )
$$

This value is the same as the value given for the acoustic impedance of fat tissue.

# Strategy for (b)

The intensity reflection coefficient for any boundary between two media is given by $a = { \frac { \left( Z _ { 2 } - Z _ { 1 } \right) ^ { 2 } } { \left( Z _ { 1 } + Z _ { 2 } \right) ^ { 2 } } }$ , and the acoustic impedance of muscle is given in Table 17.5.

# Solution for (b)

Substitute known values into $a = { \frac { \left( Z _ { 2 } - Z _ { 1 } \right) ^ { 2 } } { \left( Z _ { 1 } + Z _ { 2 } \right) ^ { 2 } } }$ to find the intensity reflection coefficient:

$$
a = { \frac { ( Z _ { 2 } - Z _ { 1 } ) ^ { 2 } } { ( Z _ { 1 } + Z _ { 2 } ) ^ { 2 } } } = { \frac { \left( 1 . 3 4 \times 1 0 ^ { 6 } \ \mathrm { k g } / ( \mathrm { m } ^ { 2 } \cdot \mathrm { s } ) - 1 . 7 0 \times 1 0 ^ { 6 } \ \mathrm { k g } / ( \mathrm { m } ^ { 2 } \cdot \mathrm { s } ) \right) ^ { 2 } } { \left( 1 . 7 0 \times 1 0 ^ { 6 } \ \mathrm { k g } / ( \mathrm { m } ^ { 2 } \cdot \mathrm { s } ) + 1 . 3 4 \times 1 0 ^ { 6 } \ \mathrm { k g } / ( \mathrm { m } ^ { 2 } \cdot \mathrm { s } ) \right) ^ { 2 } } } = 0 . 0 1 4
$$

# Discussion

This result means that only $1 . 4 \%$ of the incident intensity is reflected, with the remaining being transmitted.

The applications of ultrasound in medical diagnostics have produced untold benefits with no known risks. Diagnostic intensities are too low (about $1 0 ^ { - 2 } \ \mathrm { W } / \mathrm { m } ^ { 2 } .$ ) to cause thermal damage. More significantly, ultrasound has been in use for several decades and detailed follow-up studies do not show evidence of ill effects, quite unlike the case for xrays.

The most common ultrasound applications produce an image like that shown in Figure 17.43. The speakermicrophone broadcasts a directional beam, sweeping the beam across the area of interest. This is accomplished by having multiple ultrasound sources in the probe’s head, which are phased to interfere constructively in a given, adjustable direction. Echoes are measured as a function of position as well as depth. A computer constructs an image that reveals the shape and density of internal structures.

How much detail can ultrasound reveal? The image in Figure 17.43 is typical of low-cost systems, but that in Figure 17.44 shows the remarkable detail possible with more advanced systems, including 3D imaging. Ultrasound today is commonly used in prenatal care. Such imaging can be used to see if the fetus is developing at a normal rate, and help in the determination of serious problems early in the pregnancy. Ultrasound is also in wide use to image the chambers of the heart and the flow of blood within the beating heart, using the Doppler effect (echocardiology).

Whenever a wave is used as a probe, it is very difficult to detect details smaller than its wavelength $\lambda$ . Indeed, current technology cannot do quite this well. Abdominal scans may use a 7-MHz frequency, and the speed of sound in tissue is about $1 5 4 0 ~ \mathrm { m / s - s } \mathrm { o }$ the wavelength limit to detail would be $\begin{array} { r } { \lambda = \frac { v _ { \mathrm { W } } } { f } = \frac { 1 5 4 0 \mathrm { m / s } } { 7 \times 1 0 ^ { 6 } \mathrm { H z } } = 0 . 2 2 \mathrm { m m } } \end{array}$ . In practice, $\mathsf { 1 - m m }$ detail is attainable, which is sufficient for many purposes. Higher-frequency ultrasound would allow greater detail, but it does not penetrate as well as lower frequencies do. The accepted rule of thumb is that you can effectively scan to a depth of about $5 0 0 \lambda$ into tissue. For $7 M H z$ , this penetration limit is $5 0 0 \times 0 . 2 2 \mathrm { m m }$ , which is $0 . 1 1 {  { \mathrm { m } } }$ . Higher frequencies may be employed in smaller organs, such as the eye, but are not practical for looking deep into the body.

In addition to shape information, ultrasonic scans can produce density information superior to that found in X-rays, because the intensity of a reflected sound is related to changes in density. Sound is most strongly reflected at places where density changes are greatest.

Another major use of ultrasound in medical diagnostics is to detect motion and determine velocity through the Doppler shift of an echo, known as Doppler-shifted ultrasound. This technique is used to monitor fetal heartbeat, measure blood velocity, and detect occlusions in blood vessels, for example. (See Figure 17.45.) The magnitude of the Doppler shift in an echo is directly proportional to the velocity of whatever reflects the sound. Because an echo is involved, there is actually a double shift. The first occurs because the reflector (say a fetal heart) is a moving observer and receives a Doppler-shifted frequency. The reflector then acts as a moving source, producing a second Doppler shift.

A clever technique is used to measure the Doppler shift in an echo. The frequency of the echoed sound is superimposed on the broadcast frequency, producing beats. The beat frequency is $F _ { \mathrm { B } } = \rvert { f } _ { 1 } - f _ { 2 } \rvert$ , and so it is directly proportional to the Doppler shift $( f _ { 1 } - f _ { 2 } )$ and hence, the reflector’s velocity. The advantage in this technique is that the Doppler shift is small (because the reflector’s velocity is small), so that great accuracy would be needed to measure the shift directly. But measuring the beat frequency is easy, and it is not affected if the broadcast frequency varies somewhat. Furthermore, the beat frequency is in the audible range and can be amplified for audio feedback to the medical observer.

# Uses for Doppler-Shifted Radar

Doppler-shifted radar echoes are used to measure wind velocities in storms as well as aircraft and automobile speeds. The principle is the same as for Doppler-shifted ultrasound. There is evidence that bats and dolphins may also sense the velocity of an object (such as prey) reflecting their ultrasound signals by observing its Doppler shift.

# EXAMPLE 17.8

# Calculate Velocity of Blood: Doppler-Shifted Ultrasound

Ultrasound that has a frequency of $2 . 5 0 \mathsf { M H z }$ is sent toward blood in an artery that is moving toward the source at $2 0 . 0 \mathsf { c m / s }$ , as illustrated in Figure 17.46. Use the speed of sound in human tissue as $1 5 4 0 ~ \mathrm { m / s }$ . (Assume that the frequency of $2 . 5 0 ~ \mathsf { M H z }$ is accurate to seven significant figures.)

a. What frequency does the blood receive?   
b. What frequency returns to the source?   
c. What beat frequency is produced if the source and returning frequencies are mixed?

# Strategy

The first two questions can be answered using and $f _ { \mathrm { o b s } } = f _ { \mathrm { s } } \left( \frac { v _ { \mathrm { w } } \pm v _ { \mathrm { o b s } } } { v _ { \mathrm { w } } } \right)$ for the Doppler shift. The last question asks for beat frequency, which is the difference between the original and returning frequencies.

# Solution for (a)

(1) Identify knowns:

• The blood is a moving observer, and so the frequency it receives is given by

$$
f _ { \mathrm { o b s } } = \dot { f _ { \mathrm { s } } } \left( \frac { v _ { \mathrm { w } } \pm v _ { \mathrm { o b s } } } { v _ { \mathrm { w } } } \right) .
$$

• $v _ { \mathrm { b } }$ is the blood velocity $( \boldsymbol { v } _ { \mathrm { o b s } }$ here) and the plus sign is chosen because the motion is toward the source.

(2) Enter the given values into the equation.

$$
f _ { \mathrm { o b s } } = ( 2 , 5 0 0 , 0 0 0 \mathrm { H z } ) \left( \frac { 1 5 4 0 \mathrm { m / s } + 0 . 2 \mathrm { m / s } } { 1 5 4 0 \mathrm { m / s } } \right)
$$

(3) Calculate to find the frequency: $2 , 5 0 0 , 3 2 5 \mathsf { H z }$ .

# Solution for (b)

(1) Identify knowns:

The blood acts as a moving source.   
• The microphone acts as a stationary observer.   
• The frequency leaving the blood is 2,500,325 Hz, but it is shifted upward as given by

$$
f _ { \mathrm { o b s } } = f _ { \mathrm { s } } \left( \frac { v _ { \mathrm { w } } } { v _ { \mathrm { w } } - v _ { \mathrm { b } } } \right) .
$$

$f _ { \mathrm { o b s } }$ is the frequency received by the speaker-microphone.

The source velocity is $v _ { \boldsymbol { \mathrm { b } } }$ .   
• The minus sign is used because the motion is toward the observer.

The minus sign is used because the motion is toward the observer.

(2) Enter the given values into the equation:

$$
f _ { \mathrm { o b s } } = ( 2 , 5 0 0 , 3 2 5 \mathrm { H z } ) \left( { \frac { 1 5 4 0 { \mathrm { m / s } } } { 1 5 4 0 { \mathrm { m / s } } - 0 . 2 0 0 { \mathrm { m / s } } } } \right)
$$

(3) Calculate to find the frequency returning to the source: $2 , 5 0 0 , 6 4 9 \ H z$ .

# Solution for (c)

(1) Identify knowns:

• The beat frequency is simply the absolute value of the difference between $f _ { \mathrm { s } }$ and $f _ { \mathrm { o b s } }$ , as stated in:

$$
f _ { \mathrm { B } } = \mid f _ { \mathrm { o b s } } - f _ { \mathrm { s } } \mid .
$$

(2) Substitute known values:

$$
| 2 , 5 0 0 , 6 4 9 \mathrm { H z } - 2 , 5 0 0 , 0 0 0 \mathrm { H z } |
$$

(3) Calculate to find the beat frequency: $6 4 9 { \mathsf { H z } }$ .

# Discussion

The Doppler shifts are quite small compared with the original frequency of $2 . 5 0 ~ \mathsf { M H z }$ . It is far easier to measure the beat frequency than it is to measure the echo frequency with an accuracy great enough to see shifts of a few hundred hertz out of a couple of megahertz. Furthermore, variations in the source frequency do not greatly affect the beat frequency, because both $f _ { \mathrm { s } }$ and $f _ { \mathrm { o b s } }$ would increase or decrease. Those changes subtract out in $f _ { \mathrm { B } } = \mid f _ { \mathrm { o b s } } - f _ { \mathrm { s } } \mid$

# Industrial and Other Applications of Ultrasound

Industrial, retail, and research applications of ultrasound are common. A few are discussed here. Ultrasonic cleaners have many uses. Jewelry, machined parts, and other objects that have odd shapes and crevices are immersed in a cleaning fluid that is agitated with ultrasound typically about $4 0 ~ \mathsf { k H z }$ in frequency. The intensity is great enough to cause cavitation, which is responsible for most of the cleansing action. Because cavitationproduced shock pressures are large and well transmitted in a fluid, they reach into small crevices where even a low-surface-tension cleaning fluid might not penetrate.

Sonar is a familiar application of ultrasound. Sonar typically employs ultrasonic frequencies in the range from 30.0 to $1 0 0 ~ { \mathsf { k H z } }$ . Bats, dolphins, submarines, and even some birds use ultrasonic sonar. Echoes are analyzed to give distance and size information both for guidance and finding prey. In most sonar applications, the sound reflects quite well because the objects of interest have significantly different density than the medium in which they travel. When the Doppler shift is observed, velocity information can also be obtained. Submarine sonar can be used to obtain such information, and there is evidence that some bats also sense velocity from their echoes.

Similarly, there are a range of relatively inexpensive devices that measure distance by timing ultrasonic echoes. Many cameras, for example, use such information to focus automatically. Some doors open when their ultrasonic ranging devices detect a nearby object, and certain home security lights turn on when their ultrasonic rangers observe motion. Ultrasonic “measuring tapes” also exist to measure such things as room dimensions. Sinks in public restrooms are sometimes automated with ultrasound devices to turn faucets on and off when people wash their hands. These devices reduce the spread of germs and can conserve water.

Ultrasound is used for nondestructive testing in industry and by the military. Because ultrasound reflects well from any large change in density, it can reveal cracks and voids in solids, such as aircraft wings, that are too small to be seen with x-rays. For similar reasons, ultrasound is also good for measuring the thickness of coatings, particularly where there are several layers involved.

Basic research in solid state physics employs ultrasound. Its attenuation is related to a number of physical characteristics, making it a useful probe. Among these characteristics are structural changes such as those found in liquid crystals, the transition of a material to a superconducting phase, as well as density and other properties.



These examples of the uses of ultrasound are meant to whet the appetites of the curious, as well as to illustrate the underlying physics of ultrasound. There are many more applications, as you can easily discover for yourself.

# CHECK YOUR UNDERSTANDING

Why is it possible to use ultrasound both to observe a fetus in the womb and also to destroy cancerous tumors in the body?

# Solution

Ultrasound can be used medically at different intensities. Lower intensities do not cause damage and are used for medical imaging. Higher intensities can pulverize and destroy targeted substances in the body, such as tumors.

# Glossary

acoustic impedance property of medium that makes the propagation of sound waves more difficult   
antinode point of maximum displacement   
bow wake V-shaped disturbance created when the wave source moves faster than the wave propagation speed   
Doppler effect an alteration in the observed frequency of a sound due to motion of either the source or the observer   
Doppler shift the actual change in frequency due to relative motion of source and observer   
Doppler-shifted ultrasound a medical technique to detect motion and determine velocity through the Doppler shift of an echo   
fundamental the lowest-frequency resonance   
harmonics the term used to refer collectively to the fundamental and its overtones   
hearing the perception of sound   
infrasound sounds below $2 0 H z$   
intensity the power per unit area carried by a wave   
intensity reflection coefficient a measure of the ratio of the intensity of the wave reflected off a boundary between two media relative to the

intensity of the incident wave loudness the perception of sound intensity node point of zero displacement note basic unit of music with specific names, combined to generate tunes overtones all resonant frequencies higher than the fundamental phon the numerical unit of loudness pitch the perception of the frequency of a sound sonic boom a constructive interference of sound created by an object moving faster than sound sound a disturbance of matter that is transmitted from its source outward sound intensity level a unitless quantity telling you the level of the sound relative to a fixed standard sound pressure level the ratio of the pressure amplitude to a reference pressure timbre number and relative intensity of multiple sound frequencies tone number and relative intensity of multiple sound frequencies ultrasound sounds above 20,000 Hz

# Section Summary

# 17.1 Sound

• Sound is a disturbance of matter that is transmitted from its source outward. • Sound is one type of wave. • Hearing is the perception of sound.

# 17.2 Speed of Sound, Frequency, and Wavelength

The relationship of the speed of sound $v _ { \mathrm { w } }$ , its   
frequency $f$ , and its wavelength $\lambda$ is given by   
$v _ { \mathrm { { w } } } = f \lambda ,$   
which is the same relationship given for all waves. In air, the speed of sound is related to air temperature $T$ by   
$v _ { \mathrm { w } } = ( 3 3 1 \ \mathrm { m / s } ) \sqrt { \frac { T } { 2 7 3 \ \mathrm { K } } } .$   
$v _ { \mathrm { w } }$ is the same for all frequencies and wavelengths.

# 17.3 Sound Intensity and Sound Level

• Intensity is the same for a sound wave as was defined for all waves; it is $I = { \frac { P } { A } } ,$ where $P$ is the power crossing area . The SI unit

for $I$ is watts per meter squared. The intensity of a sound wave is also related to the pressure amplitude $\Delta p$ $I = { \frac { ( \Delta p ) ^ { 2 } } { 2 \rho v _ { \mathrm { w } } } } ,$ where $\rho$ is the density of the medium in which the sound wave travels and $v _ { \mathrm { w } }$ is the speed of sound in the medium. Sound intensity level in units of decibels (dB) is $\beta \left( \mathrm { d B } \right) { = } 1 0 \log _ { 1 0 } \left( \frac { I } { I _ { 0 } } \right) ,$ where $I _ { 0 } = 1 0 ^ { - 1 2 } \mathrm { W } / \mathrm { m } ^ { 2 }$ is the threshold intensity of hearing.

# 17.4 Doppler Effect and Sonic Booms

• The Doppler effect is an alteration in the observed frequency of a sound due to motion of either the source or the observer.   
• The actual change in frequency is called the Doppler shift.   
• A sonic boom is constructive interference of sound created by an object moving faster than sound.   
• A sonic boom is a type of bow wake created when any wave source moves faster than the wave propagation speed.   
• For a stationary observer and a moving source, the observed frequency $f _ { \mathrm { o b s } }$ is: $f _ { \mathrm { o b s } } = f _ { \mathrm { s } } \biggl ( \frac { v _ { \mathrm { w } } } { v _ { \mathrm { w } } \pm v _ { \mathrm { s } } } \biggr ) ^ { - } ,$ where $f _ { \mathrm { s } }$ is the frequency of the source, $v _ { \mathrm { s } }$ is the speed of the source, and $v _ { \mathrm { w } }$ is the speed of sound. The minus sign is used for motion toward the observer and the plus sign for motion away.   
For a stationary source and moving observer, the observed frequency is: $f _ { \mathrm { o b s } } = f _ { \mathrm { s } } \bigg ( \frac { \dot { v } _ { \mathrm { w } } \pm \dot { v } _ { \mathrm { o b s } } } { v _ { \mathrm { w } } } \bigg ) ,$ where $v _ { \mathrm { o b s } }$ is the speed of the observer.



# 17.5 Sound Interference and Resonance: Standing Waves in Air Columns

• Sound interference and resonance have the same properties as defined for all waves.   
• In air columns, the lowest-frequency resonance is called the fundamental, whereas all higher resonant frequencies are called overtones. Collectively, they are called harmonics. The resonant frequencies of a tube closed at one end are: $f _ { n } = n \frac { v _ { \mathrm { w } } } { 4 L } , n = 1 , 3 , 5 . . . ,$ $f _ { 1 }$ is the fundamental and $L$ is the length of the tube.

# Conceptual Questions

# 17.2 Speed of Sound, Frequency, and Wavelength

1. How do sound vibrations of atoms differ from thermal motion?   
2. When sound passes from one medium to another where its propagation speed is different, does its frequency or wavelength change? Explain your answer briefly.

# 17.3 Sound Intensity and Sound Level

3. Six members of a synchronized swim team wear earplugs to protect themselves against water pressure at depths, but they can still hear the music and perform the combinations in the water perfectly. One day, they were asked to leave the pool so the dive team could practice a few dives, and they tried to practice on a mat, but seemed to have a lot more difficulty. Why might this be?

• The resonant frequencies of a tube open at both ends are: $f _ { n } = n \frac { v _ { \mathrm { w } } } { 2 L } , n = 1 , 2 , 3 . . .$

# 17.6 Hearing

• The range of audible frequencies is 20 to 20,000 Hz.   
• Those sounds above $2 0 , 0 0 0 \mathsf { H z }$ are ultrasound, whereas those below $2 0 { \mathsf { H z } }$ are infrasound.   
• The perception of frequency is pitch.   
• The perception of intensity is loudness.   
• Loudness has units of phons.

# 17.7 Ultrasound

• The acoustic impedance is defined as: $Z = \rho v .$ ， $\rho$ is the density of a medium through which the sound travels and $v$ is the speed of sound through that medium.   
The intensity reflection coefficient $a$ , a measure of the ratio of the intensity of the wave reflected off a boundary between two media relative to the intensity of the incident wave, is given by $a = \frac { ( Z _ { 2 } - Z _ { 1 } ) ^ { 2 } } { ( Z _ { 1 } + Z _ { 2 } ) ^ { 2 } } .$   
The intensity reflection coefficient is a unitless quantity.

4. A community is concerned about a plan to bring train service to their downtown from the town’s outskirts. The current sound intensity level, even though the rail yard is blocks away, is 70 dB downtown. The mayor assures the public that there will be a difference of only 30 dB in sound in the downtown area. Should the townspeople be concerned? Why?

# 17.4 Doppler Effect and Sonic Booms

5. Is the Doppler shift real or just a sensory illusion?   
6. Due to efficiency considerations related to its bow wake, the supersonic transport aircraft must maintain a cruising speed that is a constant ratio to the speed of sound (a constant Mach number). If the aircraft flies from warm air into colder air, should it increase or decrease its speed? Explain your answer.   
7. When you hear a sonic boom, you often cannot see the plane that made it. Why is that?

# 17.5 Sound Interference and Resonance: Standing Waves in Air Columns

8. How does an unamplified guitar produce sounds so much more intense than those of a plucked string held taut by a simple stick?   
9. You are given two wind instruments of identical length. One is open at both ends, whereas the other is closed at one end. Which is able to produce the lowest frequency?   
10. What is the difference between an overtone and a harmonic? Are all harmonics overtones? Are all overtones harmonics?

# 17.6 Hearing

11. Why can a hearing test show that your threshold of hearing is 0 dB at $2 5 0 \mathsf { H z }$ , when Figure 17.35 implies that no one can hear such a frequency at less than 20 dB?

# 17.7 Ultrasound

12. If audible sound follows a rule of thumb similar to that for ultrasound, in terms of its absorption, would you expect the high or low frequencies from your neighbor’s stereo to penetrate into your house? How does this expectation compare with your experience?   
13. Elephants and whales are known to use infrasound to communicate over very large distances. What are the advantages of infrasound for long distance communication?   
14. It is more difficult to obtain a high-resolution ultrasound image in the abdominal region of someone who is overweight than for someone who has a slight build. Explain why this statement is accurate.   
15. Suppose you read that 210-dB ultrasound is being used to pulverize cancerous tumors. You calculate the intensity in watts per centimeter squared and find it is unreasonably high $( 1 0 ^ { 5 } \ \mathrm { W / c m } ^ { 2 } )$ ). What is a possible explanation?

# Problems & Exercises

# 17.2 Speed of Sound, Frequency, and Wavelength

1. When poked by a spear, an operatic soprano lets out a 1200-Hz shriek. What is its wavelength if the speed of sound is $3 4 5 ~ \mathsf { m } / \mathsf { s } ?$   
2. What frequency sound has a $0 . 1 0 \cdot \mathsf { m }$ wavelength when the speed of sound is $3 4 0 ~ \mathsf { m } / \mathsf { s } \ ?$   
3. Calculate the speed of sound on a day when a 1500 Hz frequency has a wavelength of $0 . 2 2 1 \mathrm { m }$ .   
4. (a) What is the speed of sound in a medium where a $1 0 0 - k H z$ frequency produces a 5.96-cm wavelength? (b) Which substance in Table 17.1 is this likely to be?   
5. Show that the speed of sound in $2 0 . 0 ^ { \circ } \mathrm { C }$ air is 343 $\mathsf { m } / \mathsf { s }$ , as claimed in the text.   
6. Air temperature in the Sahara Desert can reach $5 6 . 0 ^ { \circ } \mathrm { C }$ (about $1 3 4 ^ { \circ } \mathrm { F } )$ ). What is the speed of sound in air at that temperature?   
7. Dolphins make sounds in air and water. What is the ratio of the wavelength of a sound in air to its wavelength in seawater? Assume air temperature is $2 0 . 0 ^ { \circ } \mathrm { C }$ .   
8. A sonar echo returns to a submarine 1.20 s after being emitted. What is the distance to the object creating the echo? (Assume that the submarine is in the ocean, not in fresh water.)   
9. (a) If a submarine’s sonar can measure echo times with a precision of 0.0100 s, what is the smallest difference in distances it can detect? (Assume that the submarine is in the ocean, not in fresh water.) (b) Discuss the limits this time resolution imposes on the ability of the sonar system to detect the size and shape of the object creating the echo.   
10. A physicist at a fireworks display times the lag between seeing an explosion and hearing its sound, and finds it to be $0 . 4 0 0 \mathsf { s } .$ . (a) How far away is the explosion if air temperature is $2 4 . 0 ^ { \circ } \mathrm { C }$ and if you neglect the time taken for light to reach the physicist? (b) Calculate the distance to the explosion taking the speed of light into account. Note that this distance is negligibly greater.   
11. Suppose a bat uses sound echoes to locate its insect prey, $3 . 0 0 \mathrm { m }$ away. (See Figure 17.9.) (a) Calculate the echo times for temperatures of $5 . 0 0 ^ { \circ } \mathrm { C }$ and $3 5 . 0 ^ { \circ } \mathrm { C }$ . (b) What percent uncertainty does this cause for the bat in locating the insect? (c) Discuss the significance of this uncertainty and whether it could cause difficulties for the bat. (In practice, the bat continues to use sound as it closes in, eliminating most of any difficulties imposed by this and other effects, such as motion of the prey.)



# 17.3 Sound Intensity and Sound Level

12. What is the intensity in watts per meter squared of 85.0-dB sound?   
13. The warning tag on a lawn mower states that it produces noise at a level of 91.0 dB. What is this in watts per meter squared?   
14. A sound wave traveling in $2 0 ^ { \circ } \mathrm { C }$ air has a pressure amplitude of $0 . 5 \mathsf { P a }$ . What is the intensity of the wave?   
15. What intensity level does the sound in the preceding problem correspond to?   
16. What sound intensity level in dB is produced by earphones that create an intensity of $4 . 0 0 \times 1 0 ^ { - 2 } \ \mathrm { W } / \mathrm { m } ^ { 2 } ?$   
17. Show that an intensity of $1 0 ^ { - 1 2 } \ \mathrm { W / m } ^ { 2 }$ is the same as $1 0 ^ { - 1 6 } \ \mathrm { W / c m ^ { 2 } }$ .   
18. (a) What is the decibel level of a sound that is twice as intense as a 90.0-dB sound? (b) What is the decibel level of a sound that is one-fifth as intense as a 90.0-dB sound?   
19. (a) What is the intensity of a sound that has a level 7.00 dB lower than a $4 . 0 0 \times 1 0 ^ { - 9 } \ \mathrm { W / m } ^ { 2 }$ sound? (b) What is the intensity of a sound that is 3.00 dB higher than a $4 . 0 0 \times 1 0 ^ { - 9 } \ \mathrm { W / m } ^ { 2 }$ sound?   
20. (a) How much more intense is a sound that has a level 17.0 dB higher than another? (b) If one sound has a level 23.0 dB less than another, what is the ratio of their intensities?   
21. People with good hearing can perceive sounds as low in level as $- 8 . 0 0$ at a frequency of 3000 Hz. What is the intensity of this sound in watts per meter squared?   
22. If a large housefly $3 . 0 \mathsf { m }$ away from you makes a noise of $4 0 . 0 { \mathsf { d B } }$ , what is the noise level of 1000 flies at that distance, assuming interference has a negligible effect?   
23. Ten cars in a circle at a boom box competition produce a 120-dB sound intensity level at the center of the circle. What is the average sound intensity level produced there by each stereo, assuming interference effects can be neglected?   
24. The amplitude of a sound wave is measured in terms of its maximum gauge pressure. By what factor does the amplitude of a sound wave increase if the sound intensity level goes up by 40.0 dB?   
25. If a sound intensity level of 0 dB at $1 0 0 0 { \mathsf { H z } }$ corresponds to a maximum gauge pressure (sound amplitude) of $1 0 ^ { - 9 }$ , what is the maximum gauge pressure in a 60-dB sound? What is the maximum gauge pressure in a 120-dB sound?

26. An 8-hour exposure to a sound intensity level of 90.0 dB may cause hearing damage. What energy in joules falls on a 0.800-cm-diameter eardrum so exposed?

27. (a) Ear trumpets were never very common, but they did aid people with hearing losses by gathering sound over a large area and concentrating it on the smaller area of the eardrum. What decibel increase does an ear trumpet produce if its sound gathering area is $9 0 0 \mathrm { c m } ^ { 2 }$ and the area of the eardrum is $0 . 5 0 0 \mathrm { c m } ^ { 2 }$ , but the trumpet only has an efficiency of $5 . 0 0 \%$ in transmitting the sound to the eardrum? (b) Comment on the usefulness of the decibel increase found in part (a).

28. Sound is more effectively transmitted into a stethoscope by direct contact than through the air, and it is further intensified by being concentrated on the smaller area of the eardrum. It is reasonable to assume that sound is transmitted into a stethoscope 100 times as effectively compared with transmission though the air. What, then, is the gain in decibels produced by a stethoscope that has a sound gathering area of $1 5 . 0 \mathrm { c m } ^ { 2 }$ , and concentrates the sound onto two eardrums with a total area of $0 . 9 0 0 \mathrm { c m } ^ { 2 }$ with an efficiency of $4 0 . 0 \% ?$

29. Loudspeakers can produce intense sounds with surprisingly small energy input in spite of their low efficiencies. Calculate the power input needed to produce a 90.0-dB sound intensity level for a 12.0-cm-diameter speaker that has an efficiency of $1 . 0 0 \%$ . (This value is the sound intensity level right at the speaker.)

# 17.4 Doppler Effect and Sonic Booms

30. (a) What frequency is received by a person watching an oncoming ambulance moving at 110 $\mathsf { k m / h }$ and emitting a steady $8 0 0 - H z$ sound from its siren? The speed of sound on this day is $3 4 5 ~ \mathsf { m } / \mathsf { s }$ (b) What frequency does she receive after the ambulance has passed?   
31. (a) At an air show a jet flies directly toward the stands at a speed of $1 2 0 0 ~ \mathsf { k m / h }$ , emitting a frequency of $3 5 0 0 \mathsf { H z }$ , on a day when the speed of sound is $3 4 2 ~ \mathsf { m / s }$ . What frequency is received by the observers? (b) What frequency do they receive as the plane flies directly away from them?   
32. What frequency is received by a mouse just before being dispatched by a hawk flying at it at $2 5 . 0 \mathsf { m } / \mathsf { s }$ and emitting a screech of frequency $3 5 0 0 \ H z ?$ Take the speed of sound to be $3 3 1 \mathrm { m } / \mathsf { s }$ .   
33. A spectator at a parade receives an $8 8 8 - 1 - 1 2$ tone from an oncoming trumpeter who is playing an $8 8 0 – H z$ note. At what speed is the musician approaching if the speed of sound is $3 3 8 ~ \mathsf { m } / \mathsf { s } ?$   
34. A commuter train blows its $2 0 0 - H z$ horn as it approaches a crossing. The speed of sound is 335 $\mathsf { m } / \mathsf { s }$ . (a) An observer waiting at the crossing receives a frequency of $2 0 8 { \mathsf { H z } }$ . What is the speed of the train? (b) What frequency does the observer receive as the train moves away?   
35. Can you perceive the shift in frequency produced when you pull a tuning fork toward you at 10.0 $\mathsf { m } / \mathsf { s }$ on a day when the speed of sound is $3 4 4 ~ \mathsf { m } /$ s? To answer this question, calculate the factor by which the frequency shifts and see if it is greater than $0 . 3 0 0 \%$ .   
36. Two eagles fly directly toward one another, the first at $1 5 . 0 \ : \mathrm { m } / \mathsf { s }$ and the second at $2 0 . 0 ~ \mathrm { m } / \mathrm { s }$ . Both screech, the first one emitting a frequency of 3200 $H z$ and the second one emitting a frequency of $3 8 0 0 { \mathsf { H z } }$ . What frequencies do they receive if the speed of sound is $3 3 0 ~ \mathsf { m } / \mathsf { s } ?$   
37. What is the minimum speed at which a source must travel toward you for you to be able to hear that its frequency is Doppler shifted? That is, what speed produces a shift of $0 . 3 0 0 \%$ on a day when the speed of sound is $3 3 1 \mathsf { m } / \mathsf { s } \ ?$



# 17.5 Sound Interference and Resonance: Standing Waves in Air Columns

38. A “showy” custom-built car has two brass horns that are supposed to produce the same frequency but actually emit 263.8 and $2 6 4 . 5 \mathsf { H z }$ . What beat frequency is produced?   
39. What beat frequencies will be present: (a) If the musical notes A and C are played together (frequencies of 220 and $2 6 4 \ H z )$ ? (b) If D and F are played together (frequencies of 297 and 352 $H z ) ?$ (c) If all four are played together?   
40. What beat frequencies result if a piano hammer hits three strings that emit frequencies of 127.8, 128.1, and $\textstyle { 1 2 8 . 3 } \ H z ?$   
41. A piano tuner hears a beat every 2.00 s when listening to a $2 6 4 . 0 \dot { - } \dot { 1 } \dot { 2 }$ tuning fork and a single piano string. What are the two possible frequencies of the string?   
42. (a) What is the fundamental frequency of a $0 . 6 7 2 \cdot \mathsf { m }$ -long tube, open at both ends, on a day when the speed of sound is $3 4 4 ~ \mathrm { m / s ? }$ (b) What is the frequency of its second harmonic?   
43. If a wind instrument, such as a tuba, has a fundamental frequency of $3 2 . 0 { \mathsf { H z } }$ , what are its first three overtones? It is closed at one end. (The overtones of a real tuba are more complex than this example, because it is a tapered tube.)   
44. What are the first three overtones of a bassoon that has a fundamental frequency of $9 0 . 0 \mathsf { H z ? }$ It is open at both ends. (The overtones of a real bassoon are more complex than this example, because its double reed makes it act more like a tube closed at one end.)   
45. How long must a flute be in order to have a fundamental frequency of $2 6 2 { \mathsf { H z } }$ (this frequency corresponds to middle C on the evenly tempered chromatic scale) on a day when air temperature is $2 0 . 0 ^ { \circ } \mathrm { C } ?$ It is open at both ends.   
46. What length should an oboe have to produce a fundamental frequency of $\mathtt { 1 1 0 } \mathsf { H z }$ on a day when the speed of sound is $3 4 3 ~ \mathsf { m } / \mathsf { s } ?$ It is open at both ends.   
47. What is the length of a tube that has a fundamental frequency of ${ \mathsf { 1 7 6 } } \mathsf { H z }$ and a first overtone of $3 5 2 \mathsf { H z }$ if the speed of sound is $3 4 3 ~ \mathsf { m } /$ s?   
48. (a) Find the length of an organ pipe closed at one end that produces a fundamental frequency of $2 5 6 \mathsf { H } z$ when air temperature is $1 8 . 0 ^ { \circ } \mathrm { C }$ . (b) What is its fundamental frequency at $2 5 . 0 ^ { \circ } \mathrm { C } ?$   
49. By what fraction will the frequencies produced by a wind instrument change when air temperature goes from $1 0 . 0 ^ { \circ } \mathrm { C }$ to $3 0 . 0 ^ { \circ } \mathrm { C } ?$ That is, find the ratio of the frequencies at those temperatures.   
50. The ear canal resonates like a tube closed at one end. (See Figure 17.37.) If ear canals range in length from 1.80 to $2 . 6 0 \mathsf { c m }$ in an average population, what is the range of fundamental resonant frequencies? Take air temperature to be $3 7 . 0 ^ { \circ } \mathrm { C }$ , which is the same as body temperature. How does this result correlate with the intensity versus frequency graph (Figure 17.35 of the human ear?   
51. Calculate the first overtone in an ear canal, which resonates like a 2.40-cm-long tube closed at one end, by taking air temperature to be $3 7 . 0 ^ { \circ } \mathrm { C }$ . Is the ear particularly sensitive to such a frequency? (The resonances of the ear canal are complicated by its nonuniform shape, which we shall ignore.)



52. A crude approximation of voice production is to consider the breathing passages and mouth to be a resonating tube closed at one end. (See Figure 17.29.) (a) What is the fundamental frequency if the tube is $0 . 2 4 0 – \mathsf { m }$ long, by taking air temperature to be $3 7 . 0 ^ { \circ } \mathrm { C } ?$ (b) What would this frequency become if the person replaced the air with helium? Assume the same temperature dependence for helium as for air.

53. (a) Students in a physics lab are asked to find the length of an air column in a tube closed at one end that has a fundamental frequency of $2 5 6 \mathsf { H } z$ . They hold the tube vertically and fill it with water to the top, then lower the water while a $2 5 6 \cdot H z$ tuning fork is rung and listen for the first resonance. What is the air temperature if the resonance occurs for a length of $0 . 3 3 6 ~ \mathsf { m ? }$ (b) At what length will they observe the second resonance (first overtone)?

54. What frequencies will a $1 . 8 0 – m$ -long tube produce in the audible range at $2 0 . 0 ^ { \circ } \mathrm { C }$ if: (a) The tube is closed at one end? (b) It is open at both ends?

# 17.6 Hearing

55. The factor of $1 0 ^ { - 1 2 }$ in the range of intensities to which the ear can respond, from threshold to that causing damage after brief exposure, is truly remarkable. If you could measure distances over the same range with a single instrument and the smallest distance you could measure was $\mathsf { 1 m m }$ , what would the largest be?

56. The frequencies to which the ear responds vary by a factor of $1 0 ^ { 3 }$ . Suppose the speedometer on your car measured speeds differing by the same factor of $1 0 ^ { 3 }$ , and the greatest speed it reads is $9 0 . 0 \mathrm { m i } /$ h. What would be the slowest nonzero speed it could read?

57. What are the closest frequencies to $5 0 0 ~ { \mathsf { H } } z$ that an average person can clearly distinguish as being different in frequency from $5 0 0 ~ { \mathsf { H z ? } }$ The sounds are not present simultaneously.

58. Can the average person tell that a $2 0 0 2 - 1 1 z$ sound has a different frequency than a 1999-Hz sound without playing them simultaneously?

59. If your radio is producing an average sound intensity level of 85 dB, what is the next lowest sound intensity level that is clearly less intense?

60. Can you tell that your roommate turned up the sound on the TV if its average sound intensity level goes from 70 to 73 dB?

61. Based on the graph in Figure 17.34, what is the threshold of hearing in decibels for frequencies of 60, 400, 1000, 4000, and 1 ${ \bar { \mathsf { \Omega } } } , 0 0 0 \mathsf { \Omega } \mathsf { H z ? }$ Note that many AC electrical appliances produce $6 0 \mathsf { H z }$ , music is commonly $4 0 0 { \mathsf { H z } }$ , a reference frequency is $1 0 0 0 { \mathsf { H z } }$ , your maximum sensitivity is near 4000 ${ \sf H } z$ , and many older TVs produce a 15,750 Hz whine.

62. What sound intensity levels must sounds of frequencies 60, 3000, and $8 0 0 0 { \mathsf { H z } }$ have in order to have the same loudness as a 40-dB sound of frequency $1 0 0 0 { \mathsf { H z } }$ (that is, to have a loudness of 40 phons)?   
63. What is the approximate sound intensity level in decibels of a 600-Hz tone if it has a loudness of 20 phons? If it has a loudness of 70 phons?   
64. (a) What are the loudnesses in phons of sounds having frequencies of 200, 1000, 5000, and ${ 1 0 , 0 0 0 } \mathsf { H z }$ , if they are all at the same 60.0-dB sound intensity level? (b) If they are all at 110 dB? (c) If they are all at 20.0 dB?   
65. Suppose a person has a 50-dB hearing loss at all frequencies. By how many factors of 10 will lowintensity sounds need to be amplified to seem normal to this person? Note that smaller amplification is appropriate for more intense sounds to avoid further hearing damage.   
66. If a woman needs an amplification of $5 . 0 \times 1 0 ^ { 1 2 }$ times the threshold intensity to enable her to hear at all frequencies, what is her overall hearing loss in dB? Note that smaller amplification is appropriate for more intense sounds to avoid further damage to her hearing from levels above 90 dB.   
67. (a) What is the intensity in watts per meter squared of a just barely audible 200-Hz sound? (b) What is the intensity in watts per meter squared of a barely audible 4000-Hz sound?   
68. (a) Find the intensity in watts per meter squared of a $6 0 . 0 \substack { - \mathsf { H } z }$ sound having a loudness of 60 phons. (b) Find the intensity in watts per meter squared of a 10,000-Hz sound having a loudness of 60 phons.   
69. A person has a hearing threshold 10 dB above normal at ${ \mathsf { 1 0 0 } } \mathsf { H z }$ and 50 dB above normal at $4 0 0 0 \mathsf { H z }$ . How much more intense must a 100-Hz tone be than a $4 0 0 0 - 1 1 z$ tone if they are both barely audible to this person?   
70. A child has a hearing loss of 60 dB near $5 0 0 0 ~ { \mathsf { H z } }$ , due to noise exposure, and normal hearing elsewhere. How much more intense is a $5 0 0 0 - 1 1 z$ tone than a $4 0 0 - H z$ tone if they are both barely audible to the child?

71. What is the ratio of intensities of two sounds of identical frequency if the first is just barely discernible as louder to a person than the second?

# 17.7 Ultrasound

# Unless otherwise indicated, for problems in this section, assume that the speed of sound through human tissues is $\pmb { 1 5 4 0 } \pmb { \mathrm { m } } / \pmb { \mathrm { s } }$ .

72. What is the sound intensity level in decibels of ultrasound of intensity $1 0 ^ { 5 } \ \mathrm { W } / \mathrm { m } ^ { 2 }$ , used to pulverize tissue during surgery?   
73. Is 155-dB ultrasound in the range of intensities used for deep heating? Calculate the intensity of this ultrasound and compare this intensity with values quoted in the text.   
74. Find the sound intensity level in decibels of $2 . 0 0 \times 1 0 ^ { - 2 } \ \mathrm { W } / \mathrm { m } ^ { 2 }$ ultrasound used in medical diagnostics.   
75. The time delay between transmission and the arrival of the reflected wave of a signal using ultrasound traveling through a piece of fat tissue was $0 . 1 3 ~ \mathsf { m s }$ . At what depth did this reflection occur?   
76. In the clinical use of ultrasound, transducers are always coupled to the skin by a thin layer of gel or oil, replacing the air that would otherwise exist between the transducer and the skin. (a) Using the values of acoustic impedance given in Table 17.5 calculate the intensity reflection coefficient between transducer material and air. (b) Calculate the intensity reflection coefficient between transducer material and gel (assuming for this problem that its acoustic impedance is identical to that of water). (c) Based on the results of your calculations, explain why the gel is used.

77. (a) Calculate the minimum frequency of ultrasound that will allow you to see details as small as $0 . 2 5 0 \mathrm { m m }$ in human tissue. (b) What is the effective depth to which this sound is effective as a diagnostic probe?

78. (a) Find the size of the smallest detail observable in human tissue with 20.0-MHz ultrasound. (b) Is its effective penetration depth great enough to examine the entire eye (about $3 . 0 0 \mathsf { c m }$ is needed)? (c) What is the wavelength of such ultrasound in $0 ^ { \circ } \mathrm { C }$ air?

79. (a) Echo times are measured by diagnostic ultrasound scanners to determine distances to reflecting surfaces in a patient. What is the difference in echo times for tissues that are 3.50 and $3 . 6 0 \mathsf { c m }$ beneath the surface? (This difference is the minimum resolving time for the scanner to see details as small as $0 . 1 0 0 \mathsf { c m }$ , or $1 . 0 0 \ : \mathrm { m m }$ . Discrimination of smaller time differences is needed to see smaller details.) (b) Discuss whether the period $T$ of this ultrasound must be smaller than the minimum time resolution. If so, what is the minimum frequency of the ultrasound and is that out of the normal range for diagnostic ultrasound?

80. (a) How far apart are two layers of tissue that produce echoes having round-trip times (used to measure distances) that differ by $0 . 7 5 0 \mu \mathrm { s } \ ?$ (b) What minimum frequency must the ultrasound have to see detail this small?

81. (a) A bat uses ultrasound to find its way among trees. If this bat can detect echoes 1.00 ms apart, what minimum distance between objects can it detect? (b) Could this distance explain the difficulty that bats have finding an open door when they accidentally get into a house?

82. A dolphin is able to tell in the dark that the ultrasound echoes received from two sharks come from two different objects only if the sharks are separated by $3 . 5 0 \mathrm { m }$ , one being that much farther away than the other. (a) If the ultrasound has a frequency of $1 0 0 ~ \mathsf { k H z }$ , show this ability is not limited by its wavelength. (b) If this ability is due to the dolphin’s ability to detect the arrival times of echoes, what is the minimum time difference the dolphin can perceive?

83. A diagnostic ultrasound echo is reflected from moving blood and returns with a frequency $5 0 0 { \mathsf { H z } }$ higher than its original $2 . 0 0 ~ \mathsf { M H z }$ . What is the velocity of the blood? (Assume that the frequency of $2 . 0 0 ~ \mathsf { M H z }$ is accurate to seven significant figures and $5 0 0 ~ { \mathsf { H z } }$ is accurate to three significant figures.)

84. Ultrasound reflected from an oncoming bloodstream that is moving at $3 0 . 0 \mathsf { c m / s }$ is mixed with the original frequency of $2 . 5 0 ~ \mathsf { M H z }$ to produce beats. What is the beat frequency? (Assume that the frequency of $2 . 5 0 ~ \mathsf { M H z }$ is accurate to seven significant figures.)