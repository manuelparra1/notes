If we start on the bottom of the OSI Model,

we'll find our first layer, the physical layer.

Now, this is where bits are transmitted across the network

and includes all of the physical

and electrical characteristics of this network.

So, this is going to tell us

whether we're using an Ethernet network,

whether we're using fiber or copper cables,

whether we're using Cat5 or Cat6,

and even if we're using radio frequency

in the case of Wi-Fi.

Regardless of which method we're using

to send our data across this first layer,

it's always going to occur as bits,

and these are binary bits.

These are going to be a series of ones and zeros.

Now, each media has a different way

of representing these bits, these series of ones and zeros,

because these series of ones and zeros

are the basic building blocks of all of our data.

For example, if I'm using a copper wire,

such as in a Cat5 or a Cat6 network,

you may see that there's zero voltage on the wire

when you have a zero bit,

and then if you want to represent a one,

you might use plus 5 or negative five volts

on that copper wire.

Now, when we switch between these two modes,

this tells us whether we should read a one

or a zero on the network,

and this is called transition modulation.

Now, for the exam, you don't need to understand

the specifics of transition modulation.

But you should understand this basic concept

that on this wire,

we're going to have one level that represents a one

and another level that represents a zero.

Let me give you another example.

This time, let's pretend we're using a fiber optic cable.

Now, with fiber optic cables,

we're going to use light instead of voltages.

Now, it's similar to the way we did voltages,

but instead, when we want to represent a one,

we turn the light on.

If we want to represent a zero, we turn the light off.

Now, we can just read the state of light.

Is it on?

That's a one.

Is it off?

That's a zero.

And when there's a transition between,

that tells us between these two modes

whether we should be reading this as a one or zero.

Now, as we start understanding that,

we then have to look at the cables themself

because this is also part of our physical layer.

If we're using something like a Cat5 or a Cat6 cable,

we may have a certain connector on the end

called an RJ45, which allows us to plug that cable

into the back of a computer or into a switch.

Now, the way that connector is wired

is based on a certain standard.

We use two standards inside our network:

TIA/EIA-568A and TIA/EIA-568B.

Now, we'll talk about these

and which way these pins actually are set up

inside, this connector in a future lesson.

This is going to be important

because as we start talking about these,

this is going to tell us whether or not we're using

crossover cables or straight-thru cables.

If we use a crossover cable,

we're actually going to flip the transmission

and receive bits on the end of the cable.

So, one end will be the A standard

and one end will be the B standard.

But if we're using a straight-thru cable or a patch cable,

we're going to have the B standard on both sides.

Now, again, it's important to understand

these wiring standards,

so, we're going to spend some time on them in a future lesson

because on the exam, you may be asked

to wire up an Ethernet jack.

Maybe they're going to tell you to make a crossover cable

and you have to drag the right colors to the right pins.

That kind of a thing.

And so, to make sure you're ready for that,

we're going to cover that in a separate lesson.

Now, at this point, we've talked about having our cables,

we've talked about how we represent bits on those cables,

and we talked about how we're going to set up

the connectors of those cables.

But there's another thing we have to think about

at the physical layer,

and that's the topology of the network.

How are we actually running these cables

to physically connect the different devices together?

Well, we look at this from a Layer 1 perspective,

we can look at this based on the things we talked about

in the last section of the course.

Is it a bus, is it a ring, is it a star?

Is it a hub and spoke?

How about a full mesh, a partial mesh,

or any other topology that we discussed.

When it comes to figuring this out,

you're going to look at how they're physically cabled,

and if you drew them out,

does it make a line like a bus,

a ring, going in a circle,

or a star pattern?

And that will tell you what physical topology you have.

This, again, is a Layer 1 issue.

Another issue that we have to concern ourself with

at Layer 1 is synchronizing our communications.

We have to ask ourself how does the receiving end know

if it's ready to accept ones and zeros

that we're going to send it?

Now, this sounds like a really easy thing to do

if we're talking to each other,

but with computers, this can get much more complicated.

So, to make sure that we understand this,

we have two things that can happen.

It can either be transmitted asynchronously

or synchronously.

Now, when I'm looking at asynchronous communication,

you should be able to consider something like a voice mail.

You call up your friend, they don't answer,

and so, you leave a message so they can listen to it later.

The communication happens out of sync or out of time.

You do it and then later on,

they can go back and listen to it.

Now, in networks, this happens via a start and stop bit.

Similarly to how your friend can press Play

on their voicemail system to listen to their message,

a network can send a start bit

when it wants to start beginning the transmission

and then a stop bit to tell the other side,

hey, I'm done transmitting,

you've gotten everything I'm going to send.

Now, if we decide to go

and do communications synchronously, on the other hand,

we have to be in the same place at the same time.

So, in our previous example,

if your friend picked up the phone

and you had a conversation,

you could talk to them and they could talk to you,

this is a synchronized conversation

because you're both talking at the same time.

Now, this communication happens in real time.

That's what's great about synchronization.

Now, as far as when we start talking about this

from a network perspective,

instead of using a start and a stop bit for synchronizing,

we would use some sort of common time source.

And so, maybe we're all going to use a clock,

and every time a second passes,

we can transmit and receive,

and that tells us that we're going to do it

on the cadence of the bit.

That would be something that is synchronous.

Now, in addition to figuring out

if it's going to be asynchronous or synchronous,

you also have to figure out how you're going to utilize

the bandwidth of the cable,

and there's two main ways that you can do this.

One is called broadband and one is called baseband.

Now, broadband is going to divide our bandwidth

into separate channels.

If you have a TV service at your house,

you're probably familiar with this

because you have a single cable coming into your house,

but it carries 200 or more channels.

The user, then, is going to choose a single channel

and the rest are going to be filtered out.

In opposition to this, we have baseband,

where you're going to use all of the frequency of the cable

all of the time.

So, a telephone, for instance, uses baseband communication,

which means that when you pick up the phone,

you're using all of the bandwidth

allocated to that phone line.

This doesn't hold true with the cable TV signal, right?

Because we had 200 channels

all using some of that bandwidth,

but we only pulled out the ones we wanted.

For this reason,

we can only make one call at a time when using a phone,

but we can have 200 channels or more on our TV.

Now, when we use baseband,

we're going to use a reference clock

that allows us to send the information

for both the sender and the receiver at the certain time.

By using this reference clock,

this is an example of using a synchronous communication.

Another good example of a baseband network

is a wired home Ethernet network

because this is going to use all of the frequency

that's available on your cable, giving you more bandwidth

than you would if you had a broadband area.

Now, in this case, if we have a single baseband

using up all of the bandwidth,

we need to figure out how to get more out of it.

And so, to do this,

we have a couple of different mechanisms we can do.

And the first one of these

is what's known as time-division multiplexing.

In this mode, each session is going to take turns

using a dedicated time slot

to get part of that bandwidth from the baseband.

Now, an easy analogy of this

is if you have a house with a single TV in it

but you have four family members.

Everyone wants to watch TV, but there's only one TV,

so they're going to have to take turns

picking what program is going to be on.

Now, in a pure time-division multiplexing environment,

each person is going to be assigned a time slot

and they can pick whatever TV show they want

during that time slot.

Now, this may or may not line up

with the time that their show is actually on

and that could cause a problem, right?

So, we have the second method

called statistical time-division multiplexing or StatTDM.

This is a more efficient version

of time-division multiplexing

because it's going to dynamically allocate these time slots

based on when people need it.

So, if we take our TV example,

maybe, for example, I want to go down

and nobody is watching TV at eight o'clock,

but it wasn't my time slot.

Well, under time-division multiplexing,

I couldn't turn on the TV

because it wasn't my time slot.

But with StatTDM, I can,

because as long as nobody is using the TV,

anyone is free to use it.

Everyone is going to take turns based on their necessity,

not based on the time itself.

So, instead, when I start watching the TV at eighth o'clock,

then after my 30 minutes is up,

I'm going to get off at 8:30 so somebody else can get on

even though my assigned time slot under TDM

might have been something like nine to 9:30.

Now, our last method is what's known

as frequency-division multiplexing or FDM.

This is going to involve taking the medium, that cable,

and splitting it up into channels

similar to the way we do in broadband.

So, if I take a single cable and I break it up

into 50, 100, or 200 different frequencies,

then each person can get a small portion

of frequency allotted to them

and they can use it as much as they want.

Now, for the exam, the good news

is you don't need to memorize TDM, StatTDM, and FDM,

but rather, you just need to understand that multiplexing

involves taking some limited amount of resource

and using it more efficiently.

In the real world, you may come across

these multiplexing techniques,

especially if you start working

as a network engineer or a network architect,

and that's why I want to introduce them to you.

But for the Network+ Exam,

just remember, multiplexing allows multiple people

to use a baseband connection at the same time.

The final thing we need to talk about in this lesson

is some examples of physical or Layer 1 devices.

The most common one is going to be a cable.

So, if I have a fiber optic cable

or an Ethernet cable or a coaxial cable,

these are all different types of media.

And if I have different types of media,

that's considered a Layer 1 device.

The reason is whatever goes in one end of the cable

is going to come out the other end of the cable.

So, if I have a fiber optic cable

and I put light in one end,

I'm going to get light out the other end.

That's a physical response,

a physical layer of the OSI Model.

Additionally, beyond wired cables,

we also have wireless things,

things like Bluetooth and Wi-Fi

and near field communication.

All of these radio frequencies make up the media

at Layer 1 for those type of networks.

The final example is infrastructure devices,

and that will be things like hubs, access points,

and media converters.

All of these devices operate at the bit layer.

This is going to be a function

to just simply repeat what they get.

So, if I have a hub, whatever goes in port one of the hub

is coming out of ports two, three, and four.

Whatever comes in gets repeated out.

The same thing with the media converter.

If I have something coming in over coaxial,

it's going to get converted through media

and pushed out over fiber optic.

That device is simply doing it at the physical layer.

Whatever comes in is going to go out.

There's no logic to it, there's no intelligence to it.

Layer 1 devices simply repeat whatever they're told.

Now, we'll talk about some other infrastructure devices

as we get into Layers 2 and 3 and 4

but for right now, I want you to remember

Layer 1 is dumb devices.

They're simply repeaters.

Whatever they take in, they send it right back out.
