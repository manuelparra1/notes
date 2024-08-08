Now that we're at the network layer,

we're concerned with routing.

Layer 3 is all about how we're going to forward traffic,

which we refer to as routing using logical addresses.

For example, your computer has an IP address.

And that IP address is either going to be an IP version 4

or an IP version 6 address, or both.

Now, both of these are considered layer 3 protocols.

And we're going to talk more about them

as we go through this course.

Now, the other thing we're going to be concerned with here

is logical addressing.

I mentioned that IPv4 and IPv6

are two types of logical addresses,

but they're not the only logical addressing schemes

that are out there.

They're just the most common and most popular these days.

Now, we're also going to be concerned

with what's known as switching.

And here, when we talk about switching,

we're actually talking about layer 3 switching,

which is called routing.

Now, I know this gets confusing

because you're using the term switching

to refer to the function of routing,

and when we talk about switches,

the devices being layer 2 devices.

So, you have to keep this straight in your head.

Switches, the physical device, are layer 2.

Switching is another term for routing,

which is how we transfer things

at the network layer, layer 3.

Now, as we talk about all these, another thing that comes up

is how we're going to do route discovery and selection.

Now, basically, that means how do I know

which way I want the traffic to go?

We're going to talk a little bit more about that, too,

as we go through this lesson

because we're going to talk about connection services

and bandwidth utilization and multiplexing strategies.

All of these is at the layer 3 of the network layer.

So, to start diving in deeper into these concepts,

let's start out with logical addresses.

There are lots of different routed protocols

that have been used over the years.

Back in the '80s and '90s,

there was AppleTalk for Apple computers.

And if you used a Windows or a Novell Network computer,

you might have used IPX,

which was the Internetwork Packet Exchange.

Now, neither of these two are important

for the Network+ certification,

but it is something that I want to bring up

because you may hear these terms.

Really, what happened was these were both killed off

by Internet Protocol, which is known as IP.

This became the common protocol that everyone uses

on all networks and therefore,

we didn't need AppleTalk and we didn't need IPX anymore.

But the point is, at layer 3, it's not just IP.

There are other protocols that you could use in layer 3.

IP is just the most common.

Now, some of those are still existing

on some legacy systems,

which means old systems in some corporate network.

But the routing protocol of the Internet that we use

and the Internet you have at home

and the network you have at home is going to be known as IP.

IP comes in two variants, as I said before, IPv4 and IPv6.

Now, if you look on the screen here,

there's an example of an IP address.

It's written as 172

.16

.254

.1.

Now, we're going to look at more IP addresses

in a separate lesson as we dig deeper into routing later on.

For the time being, I want you to think of an IP address

anytime you see a number that looks like this.

There's going to be four sets of numbers, separated by dots.

This is called a dotted-octet notation,

and this is what an IPv4 address is going to look like.

Now, how shall we actually forward

or route the data across our networks?

This is really the big question at layer 3.

And there are three main ways for us to do this.

You can use packet switching,

circuit switching, or message switching.

The most commonly used one in your network

is going to be routing,

which is also known as packet switching.

This is where data is divided into packets

and then each packet is forwarded on

based on its IP address.

Now, when I think of routing, I like to think about this

as if I'm going to write a letter and send it to my mom.

Let's say I put that letter in an envelope,

and on the outside of the envelope,

I'm going to write the address of my mom on it.

I put her city and her state and the zip code.

Now, I put that in the mailbox,

and the mail carrier is going to take it to a central location.

Here, they're going to figure out what state it goes to

and then, they're going to send it to that state's post office.

Once it's in that state, it's going to go down even further,

and they're going to go down to the city-level post office.

And then, from that city-level post office,

they're going to look at where the street address is,

get it to the right street,

and eventually get it to her house on that street.

The same kind of concept works with IP addresses.

And that's the idea here.

It's going to keep going and switching that packet

from place to place until it gets to its final destination.

In the case of my envelope, to my mom's address.

Now, that's the way that packet switching

is going to work for us.

Every time I send a letter out,

it might take a different route to get there.

And I really don't care which route it takes,

as long as it gets to its final destination.

It's the same thing with our packets in the network.

When I talk about circuit switching, though,

this is where we want to have

the same path each and every time.

We're going to get a dedicated communications link

that's established between our two devices.

And if I pick up the phone to make a phone call,

I'm actually going to make a virtual connection from my phone

over to the other receiver's phone on the other end.

So, if I pick up the phone to call you,

there's going to be a temporary connection made

between my phone and your phone,

and all of the data that we're talking back and forth

will go across the same path to get from me to you.

The whole time we have this conversation going on,

that's what's going to happen.

That's what we call a circuit switch connection,

which is different than the packet switch connection

of using an envelope where we don't care

where all those envelopes go

as long as they got to the right place at the end.

Now, when we hang up the phone

and we go to make another call,

it could take a different path, and that's okay.

But for the entire session of us having our phone call,

we want the same path,

and that's what circuit switching allows us to do.

Now, the third type of switching we have

is known as message switching.

And with message switching,

this is where all the data is divided into messages,

and they're similar to packet switching in this idea.

But the messages can actually be stored

and forwarded, more like email.

So, if you go back to my mail example,

maybe it gets to my mom's state,

but the post office is closed because it's Sunday.

So, what happens is they drop

all those envelopes on the floor.

Now, it's going to be held there until they open again

on Monday and somebody's going to be able to pick it up,

figure out where it goes, and push it along.

This is what happens

when you're dealing with message switching

because it has a store and forward capability.

If we were using just packet switching,

what would end up happening is if it got to the post office

and the post office was closed,

it would actually just shred that envelope

and nobody would ever see it.

That's a bad thing if we want to make sure

the data is going to get where it's going,

and that's why message switching can be very useful for us.

Now, almost all of our networks nowadays

and the ones you utilize

are going to be using packet switching, though.

And the reason is we have other methods that will check

if something is not getting to the distant end,

and will be resent over another path

until it finally gets there.

So, unless you're dealing

with some kind of big backend networks,

you're not really going to see something like circuit switching

or message switching in your normal everyday networks.

Your home network, my small office network,

and most of the Internet

actually works using packet switching.

Now, the second thing we have to talk about

is route discovery and selection,

how are we going to decide which path

we're going to take to send that message.

Well, routers are going to maintain a routing table

so, they can understand how to forward a packet

based on the destination IP of where it wants to get to.

There are lots of different ways that it can do this,

and they can do this either as a static route

or dynamically-assigned route

using a routing protocol like RIP, OSPF, EIGRP,

and many others.

Now, we're going to talk about many of those

later on in this course, so we're not going to talk

specifically about how it works right now.

We're just going to put that to the side.

But I want you to remember that routing protocols

help us decide how data is going to flow across the network

and how the routers are going to communicate that information.

For now, let's just use the example on the screen

to give us a really basic idea of how routing works.

Let's say that I'm sitting in router number five

at the bottom-right corner,

and I want to get to router number one.

Well, how should I do it?

I can go from five to four to one, and that would work,

but I can also go from five to four to three to two to one,

and that would also work.

So, how do I know which way

is going to be the best way for me to go?

Well, if I end up using a dynamic protocol,

all of these routers continually talk

to each other all the time, and they tell each other

which way they know how to get to other routers

and which one is the best and fastest route.

So, if you think about this like streets,

when you type into your GPS

that you want to go from point A to point B

to get to the grocery store,

it may take you three or four different ways

depending on the time of day, the traffic,

the congestion, and a number of other factors.

Routers are doing the exact same thing.

They all talk to each other and they say,

hey, I've got a better way for you

to get from point A to point B

because there's too much traffic on this direction,

so, you should go and take this other route, instead.

That's the idea with route discovery and route selection.

Now, the next thing we need to talk about here

is connection services.

And connection services are going to augment

our layer 2 connection services

that we talked about previously

and provide us with some additional reliability.

Again, we're going to have some more flow control added here,

and this is going to prevent the sender

from sending data faster than the receiver can get it.

Again, that's the way that we have flow control there,

so it can say, hey, hey, hey, slow down,

you're sending me too much data,

or speed up, I can take more, I'm ready for more.

We also have this thing called packet reordering.

Now, packet reordering is really important

because it allows us to take this big chunk of data,

cut it up into little pieces of packets,

and then, send all those packets off in different directions

to get to their final destination.

Now, the problem is sometimes these packets

are going to arrive at the destination in the wrong order.

And so, packet reordering allows them

to get all this data at the end destination at the receiver,

and they can take and say, okay,

I got packet one and packet five and packet two

and packet four and packet three,

and then, I'm going to put them in the right order,

one, two, three, four, five,

and then I can put that data back together in what it is,

and now, I have the full piece of data together.

The benefit here is that because of routing,

each packet gets numbered and sequenced,

and so, even if they get to the other end out of order,

we can put them back into the right order

and read them as a coherent message.

The next thing we need to talk about here at layer 3

is known as ICMP or the Internet Control Message Protocol.

ICMP is used to send messages

and operational information to an IP destination.

The most commonly used one is known as ping, P-I-N-G.

And we're going to talk specifically about that tool

in our troubleshooting lecture.

As you can see in this example,

we can send out a single packet as a test to example.com.

And when it comes back,

we can then say if that site is up or down.

This is what ping does.

It sends out a packet and tells us

if it was received or not by the distant end

and how long it took.

In this case, we got a response back five different times,

showing that it was up

and we were able to get to that distant end.

Now, this is not a tool that's used regularly

by end-user applications,

but it is used by us as administrators

to help troubleshoot our network and figure out

what is up and what is down and what isn't working.

Again, the most commonly used one here is going to be ping,

but there's another variation of it known as traceroute,

which will trace the route that a packet takes

through the network and tells you every single router

along the way as it goes through,

essentially doing a large series of pings

through each and every router

so you could figure out which routes were up

and which routes were down.

Now, what are some examples of layer 3 devices

that we need to remember for the exam?

Well, the first two you have to remember

are routers and multilayer switches.

A router looks like this die icon here.

You can see it's on the screen.

It's a circle with four arrows, and this is a depiction

of what a router looks like in a logical diagram.

Now, a multilayer switch works

like a regular switch and a router combined.

So, it has both features of a layer 2 switch

and a layer 3 router in the single device,

which is why it's considered a layer 3 device.

Again, for the exam, remember that a switch

is always a layer 2 device unless they specifically tell you

that it is a multilayer switch.

If it's a multilayer switch,

it is going to be considered a layer 3 device.

Now, some other things that we have

is going to be things like IPv4 and IPv6.

These are both layer 3 protocols.

We also have ICMP, the Internet Control Message Protocol,

that we just talked about that's used in troubleshooting.

All of these are found at layer 3.

The best one to remember is IP and routers

because these are going to be the most common ones

you're going to see on test day

if they ask you for examples of a layer 3 device.
