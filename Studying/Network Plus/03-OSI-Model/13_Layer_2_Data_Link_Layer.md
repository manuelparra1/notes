Welcome to Layer 2 of the OSI model, the data link layer.

In the data link layer,

we're going to package up the bits we got from Layer 1

and put those into frames

and then, we're going to take those frames

and transmit them throughout the network

while performing some error detection, correction,

identifying unique network devices using MAC addresses,

and we're going to provide some flow control.

Now, a MAC address is a media access control address

which is a means for identifying a device physically

and allowing it to operate on a logical topology.

So, when we started talking about physical topologies

in the last lesson in the last layer,

we dealt with things physically,

but now, we have to deal with things on a logical level.

These MAC addresses are incredibly important

for dealing with switches and other Layer 2 devices.

When it comes to identifying MAC addresses,

every manufacturer of a network card

assigns a unique 48-bit physical addressing system

to every network interface card they produce.

As you can see here,

we have 12-digit hexadecimal numbers

that are used to represent these MAC addresses.

These MAC addresses are always written hexadecimally

wherein each of the letters or numbers

is considered four bits.

The first 24 bits or the six letters as you can see here

identifies the particular vendor who made that card.

In our example, we have D2:51:F1

and this is going to uniquely identify

whichever person made this card.

I like to think about this like a social security number

in the United States.

If you look at the first three digits,

it's going to identify the state

and the year that person was born in.

For instance, if my social security number was 123456789,

the first three digits might say when and where I was born.

Maybe it was California in the year 1955

and those other six digits are going to uniquely identify me.

Well, this is the same thing that happens

with a MAC address.

The first half of the MAC address, the first six digits,

is going to tell us who made it.

Was it made by Apple, Dell, Raw Link, or whatever?

The second half is going to represent

the exact machine it belongs to.

This is important for our logical topology

because we can look at the MAC address

and observe the flow of data going through our networks.

And at this point, we don't really care

how these devices are physically connected.

The issue at that point is a Level 1 issue.

But now at Layer 2,

we care about who's turn it is to talk and transmit

so other devices aren't talking over each other.

For example, when I teach this course

in a classroom environment,

instead of all of the students

shouting out their answers at once,

we use the system of raising our hands.

We wait for the teacher to call on one of the students

and then, we can let them ask a question.

This is how we control the information flow

so that everyone can hear each other.

In a network, we use electronic mechanisms

to do this same thing.

Now, logical link control

is going to provide connection services

and allow your recipients to acknowledge

the messages have actually gotten

where you thought they were going.

So, for example, if I called up

and I asked if you got my phone call,

you could say yes

and that would acknowledge the receipt of that

and then, we can move on to the next message.

Logical link control does this for our networks.

And because of this,

it's the most basic form of flow control.

Essentially, it's going to limit the amount of data

that a sender can send at once

and allow the receiver to keep from being overwhelmed.

So, if I go back to my classroom example,

if I'm sitting there and I'm moving too quickly,

a student might raise their hand and say,

"Hey Jason, I don't understand this.

"Can you slow down and repeat it?"

In the case of this video,

you can just pause or go back and watch that part again,

but in a classroom, they can't

so they may ask me to repeat it.

Logical link control, it similarly does the same thing,

allowing a device to make this request

for either less information at a time

or to replay that information.

Logical link control also gives us

some basic error control functions

such as allowing the receiver to inform the sender

if their data frame wasn't received

or if it was received corrupted

and it does this by using a checksum.

Now, since everything it receives

is just a series of ones and zeroes,

the receiver is going to add all of these up

and the last bit will either be even or odd.

If it matches, they add them all up and they're even,

then, it's going to assume that this was good

if you have received a zero, meaning it was even.

If the last bit was odd, meaning it was a one,

and they added up all the numbers

and they got an odd number,

that means it was good, as well.

But if not, they can figure that something was bad

and then ask for a retransmission of the frame.

Now, communication can be synchronized across Layer 2

according to three different schemes.

We have something known as isochronous mode

which happens when the networks use a common reference clock

similar to synchronous

yet they also create time slots for transmissions,

much like we did with time division multiplexing.

This has less overhead than either of the other two modes

because both devices know when they can communicate

and for exactly how long.

The second method we can use is known as synchronous method

and this is much like we use back in Layer 1.

It's going to involve devices using the same clock.

But the reason it's different from isochronous

is that this is going to allow us

to have beginning and ending frames

and special control characters

to tell us when we're going to start

and when we're going to end based on those beats.

For example, if I use it in music,

I have songs that have various time signatures,

things like 3/4 or 4/4 timing.

This tells us how many beats are in each measure.

Our networks operate much the same way

in that our devices can only communicate

at frequencies specified by these particular clock cycles.

Because of this, there isn't a lot of gap time

that isn't already properly utilized

and this becomes a major drawback for synchronized mode.

And finally, of course, we have asynchronous

which is going to allow each of our network devices

to reference their own clock cycles

and use their own start and stop bits.

In this way, there's no real control

over when the devices are allowed to communicate, though,

and that becomes the major drawback here.

Now, when we look at Layer 2 devices,

we have things like network interface cards,

bridges, and switches.

In contrast to how a hub is a dumb machine

that simply relies on a message coming in

and repeating it back out,

switches are smarter.

They can actually use logic

to learn which physical ports are attached to which devices

based on their MAC addresses.

And in this way,

they can send data to specific devices in the network,

allowing us to pick up and choose

different lines of communication to go to different areas.

Now, we'll talk all about how this works

and how these switches do these,

including things like CAM tables using the MAC addresses

and how they're doing the switching across the network

in later lessons and we'll go into depth in that

because you will need to understand that

to understand how networks really work.

But for right now,

just remember that switches, bridges, and MAC addresses

are three great examples of things that operate at Layer 2,

the data link layer.
