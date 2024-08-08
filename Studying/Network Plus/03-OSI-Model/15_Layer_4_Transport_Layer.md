Layer 4, the transport layer.

Now, the transport layer is our dividing line

between what we call the upper layers of the OSI model

and the lower layers of that OSI model.

Now, we've already covered the lower layers

when we talked about the physical,

the data link, and the network layers.

And so now, we're going to move into the upper layers,

starting with this layer, the transport layer,

the session layer, the presentation layer,

and the application layer.

Now, in the next couple of lessons,

we're going to cover each of these as we go forward.

Now, segment is our datatype here

when we're dealing with the transport layer.

When we deal with segments and datagrams,

we're talking about the transport layer.

Now, as we talk about datagrams,

we're going to go into those a little bit more later in depth.

But for now, let's focus on the two protocols

that we have inside layer 4,

which are the TCP and the UDP protocols.

And we're also going to introduce

a couple of extra reliability features here

known as windowing and buffering.

Now, what is TCP?

TCP is a transmission control protocol.

It is a connection-oriented protocol,

which means it's a reliable way to transport segments

across our network.

Now, if a segment has dropped,

the protocol will actually ask for acknowledgment

each and every time.

If it doesn't get that acknowledgement,

it's going to resend that piece of information.

That's why we call this connection full protocol

because it has this two-way type of information

where I'm sending you information

and I'm verifying you actually got it

by listening that you got it and you give me a response.

Now, let's look at this little diagram here

on the screen for a second.

You're going to see that I have a client on the left

and a server on the right.

Now, the client is going to send what's called a SYN packet

or a synchronization packet over to the server.

Now, when the server gets that,

it's going to send back a synchronization acknowledgment

to the client known as a SYN-ACK.

Now, when the client gets that acknowledgement,

it's going to send back its own acknowledgement to the server.

This is known as the ACK.

Now, when we do this SYN, SYN-ACK, ACK,

this is what we refer to as a three-way handshake.

Essentially, it's the client going, hey server,

are you ready to get some information?

And then the server says, sure, why not?

Send me some information.

And the client says, okay, here it comes.

And then, the transmission is going to begin

because we've established that three-way handshake

and we know that both sides are ready to communicate.

Now, are you ready?

Yes, I am, here it comes.

Now, every time this data, which we call a segment,

is sent across the network,

there is going to be an acknowledgment that it was received

and that tells us there was successful

two-way communication occurring.

Now, if the server is expecting to get 100 pieces

of information, but it only got 98 of those,

it's going to say to the client,

hey, you told me you're going to send me 100 things

but you only sent me 98.

Send me over those two things that I'm missing.

And then a retransmission occurs.

This way, the communication can go forth

and we can always make sure we're getting

what we're supposed to because we have this resending

of the packets across the network.

Now, this is used for all network data

that needs to be assured to get to its final destination.

I like to think about this like certified mail.

If I want to send a message to the IRS, for example,

I want to make sure that they get it

and that doesn't get lost in the mail.

So, I might pay a little extra money

to get a certified receipt that when it gets there,

they have to sign it and that gets mailed back to me.

This way, when I get that receipt back,

I know that the IRS got my mail package.

That's the way TCP works.

Now, on the other hand, we have another protocol

known as UDP.

UDP is what we call a connectionless protocol,

meaning, it doesn't have to wait for connections.

UDP stands for User Datagram Protocol

and the reason why we call it a datagram

is because if you're using UDP,

you're using this type of data,

it's called a datagram.

And so, for the exam, I want you to remember

that layer 4 is for segments almost exclusively

because we use it with TCP.

But if you're using UDP, this is now called a datagram.

So, if you have a datagram or a segment,

you're in layer 4.

Now, when we talk about UDP, UDP is unreliable

and it transmits segments called datagrams

and if they're dropped,

the sender will never even know that it happened.

Now, why would I want to send stuff

where the sender isn't aware of it

and I don't get any kind of receipt?

Well, UDP is really good for audio and visual streaming

because you send a lot of data

and there's a lot less overhead when you use UDP

because we don't have that constant three-way handshake

to establish it and we don't have

all the checks and balances that are associated

by using TCP.

So, by using UDP, you can really increase the performance

of your network because you're going to have

zero retransmissions,

you're just going to end up dropping information.

Now, isn't that a bad thing?

Why would we want to drop information?

Well, for certain applications, it really doesn't matter.

For example, you're streaming this video right now

and if I dropped out for one hundredth of a second,

would you even notice?

Well, you probably wouldn't.

And that's why UDP is so good

because we can drop one 100th of the time here

and you're really never even going to notice it

and there won't be a retransmission.

But with TCP, it's going to lead to a lot more buffering

because you have to wait and then get resent to you

and then put it in the right place and then play it back.

And so, because of that acknowledgement and that overhead

for every single second of this video,

it's going to end up making a lot larger

and use a lot more bandwidth.

And that's one of the big reasons why we use UDP

for video streaming and audio streaming.

Now, let's do a quick little summary here of TCP versus UDP

because this is a really, really important concept.

In fact, if you have your notes out right now,

I would write down this chart

that I'm going to tell you right now

as we talk about TCP versus UDP

because it really is that important.

Now first, TCP is reliable.

It has a three-way handshake where UDP is not very reliable,

it's an unreliable protocol

because there is no three-way handshake.

TCP is what we call connection-oriented

or a connectionfull protocol

because we have that three-way handshake

in the acknowledgements but UDP is connectionless.

It's a fire and forget method.

I just start sending out information

and hopefully you're going to get it.

TCP uses segment retransmission and flow control

that's being handled through windowing,

which we're going to talk about more in just a second.

UDP, on the other hand, there is no retransmission

and no windowing.

With TCP, we have segmentation of our sequencing

of all of our different segments.

With UDP, there is no sequencing.

Now, what this means is, as I send everything out,

I'm going to send it out in the proper order from one to 100.

I'll do this for both TCP and UDP.

Now, if you miss some of those pieces,

or they arrive in a different order

because they take different paths over the network,

with TCP, they're sequencing

so it knows that you have one to 1,000

and it puts them back in the right sequence.

With UDP, whatever they come in as,

that's how it's going to broadcast it.

And so, it can be coming in 1, 50, 2, 500,

3, 4, 5, 6, 20,

in any random order like that

and that's how you're going to hear it.

So, if video, you may hear a little bit of jumpiness,

or a little bit of high-pitch squeaks

or something like that

because one of those frames may have come out of order.

Now, when we go back to TCP, it is going to acknowledge

each of those segments.

And so, we have acknowledgment.

If I don't get it, I know that I didn't get it

and I can get it retransmitted to me and then get it again.

With UDP, there is no acknowledgement.

So, again, UDP has a lot less overhead

because there's no connection,

no windowing, no retransmission, no sequencing,

and no acknowledgement.

Now, if you have to get something there

and you want to make sure the person got it,

you really have to use TCP as your protocol of choice.

And that's why we really are going to use TCP

for things like banking and websites and ecommerce

and things like that.

But if we have something that has a lot of data

like audio or video streaming,

UDP really does well with that

because we don't need to get

every single piece of that file.

We can skip a little bit here and there and that's okay.

Now, earlier in the lesson,

I mentioned a concept known as windowing

and I said, we'd get to it later.

Well, here we are.

We're going to talk about windowing.

Now, what is windowing?

Windowing is going to allow the clients

to adjust the amount of data in each segment

as it goes through the transmission.

This way, we can continually adjust

to either send more or fewer pieces of data

for each segment that's being transmitted.

So, the whole idea here with windowing

is that if you're sending data

and you're getting a lot of retransmissions,

well, you might be sending too much information.

So, you need to back that down

and close the window a little bit.

So, you'll send less each time.

Now, if you're not getting any retransmissions,

it means you're probably not going fast enough.

So, instead, we can open up that window

and send more data with each of those segments.

And then, if we start getting

a lot more of those retransmissions happening again,

well, we start closing that window down.

And so, always we're opening and closing the window

to maximize our throughput and our bandwidth here.

So, if you ever copied a file over a network

on a Windows machine, you've probably seen

where it starts that movie file and it starts saying,

hey, you have 20 minutes remaining

and then it drops down to five minutes remaining,

then it jumps up to 50 minutes remaining,

and then 30 minutes remaining, and then an hour,

and then it goes down to three minutes.

And it has a really hard time estimating

how long it's going to take to move that really large file

off of your shared drive and onto your Windows computer.

Now, why is that?

Well, that's windowing at work.

What's happening here is that as there's issues

on the network, and there's a lot more retransmissions,

the window decreases become smaller

and that means, we have to send more segments

to get all that data across, which takes more time.

Now, as things go better,

and the network starts flowing again,

that window opens up and we can send less segments

with more data each time and that's going to end up

decreasing the time or making it go down.

So, what happens here is as you can see on the screen,

let's say that little green thing is what I'm sending

and I start sending the information over

but that red starts creeping up

to where we start to not being able to keep up with it.

So, we'll come back down and then the red can creep up again

and then, we'll come back down and we'll keep doing that.

Hopefully, the red and the green here

will eventually match at a higher level

than it was starting with.

As soon as we open up that window and close that window,

we can start out slow and then we can go faster

by opening up that window and faster and faster

until we have problems and then we'll start

closing it down again.

And we'll keep doing that over and over and over again,

until we get the best bandwidth we can

as we try to push as much as we can.

So, for example, if I started counting numbers to you,

I'm going to start going slow.

One, two, three, that's pretty slow, right?

You'll say okay, okay, I got it, Jason.

You can go faster.

So, I start talking faster.

One, two, three, four, five, okay?

That's still good, let's try again.

One, two, three, four, five,

oh, wait, wait, wait, wait, that's too fast, Jason.

Okay, let me slow down.

One, two, three, four, five, you got it?

Okay, and we keep doing that.

That's the idea of windowing.

I'll speed up and I'll slow down

until you don't have any errors copying down

what I'm saying.

That's the whole idea here.

And we want to be able to send as much information to you

as quickly as possible

with the least amount of retransmissions

but still getting the maximum throughput.

Now, the next concept we want to talk about is buffering.

If you've ever watched online video,

you've probably dealt with buffering before.

Now, devices such as routers have a special memory in them

that will store segments if the bandwidth

isn't readily available.

Now, this is called the buffer.

So, when it becomes available,

it'll go ahead and start transmitting out the contents

of that buffer and clear itself out.

The same thing happens when you try to load a video.

If the network is congested,

it will take in a lot of information at first

in anticipation of the fact

that you're going to watch it faster,

then, you're going to be able to download the rest of the video.

And so, this is the idea with our buffering

our routers, as well.

So, if the buffer is going to overflow, though,

and on a router you only have so much space

and you start putting too much information there

cause you can't send it out,

then what's going to end up happening?

You run out of memory.

And when you run out of memory, the segment's will drop.

So, let's look at an example of how buffering

is going to work.

Let's take a look at the buffer on the router

and here we have router four in our diagram.

Notice how it's kind of the central point of this diagram.

Now, I have stuff coming into it from router number six,

and router number one and router number three.

So, if I look at all of those, there's 100 megabits,

100 megabits, and 10 megabits.

That's a possibility of 210 megabits per second

of information going into router four.

Now, if it needs to send that information out

to router five, and there's only a 50 megabit connection,

you can see pretty quickly

that there's going to be a bottleneck here.

Now, what's going to end up happening for us

is that router four is going to have to catch

all that extra information in its buffer.

And when it has more availability,

it'll send that information out to router five

and clear its buffer.

You may ask, why would we design a network this way?

Well, often what's happening here

is there isn't necessarily going to be 100% utilization

from router four to router five.

Maybe that's our exterior one connection

going out to the Internet.

In fact, router one may only be sending you

10 or 15 megabits per second right now.

And router three might be sending you 30.

And router six might be sending you one

which is all added together less than 50.

So, no buffering would occur.

Now, there's also the possibility that router one

and router three sends us more information.

And that can cause buffering to occur

because router four can't send enough data out

to router five over that 50 megabit per second connection.

So, this is the idea, we want to buffer things and hold it

and then as we have room, we can send that information out,

clear the buffer, and keep on moving.

Because when we look at your networks,

the chances are not every device is communicating

to 100% of its capability all of the time.

And so, by doing this, we can pay for a smaller connection

to the outside world that 50 megabit connection,

as opposed to paying for a large

and expensive fiber connection of one gigabit per second.

So, we can keep our costs down

by knowing what our utilization is over our network

for the long period of time.

Now, that gets into some more advanced concepts

that as you work as a network engineer,

you'll start working on those designs

and as bandwidth keeps getting cheaper,

it becomes less and less important for us,

at least in the small office, home office environment.

But in large corporations, this is a big deal.

Now, what are some examples of layer 4 devices?

Well, we have TCP and UDP as our protocols for layer 4.

So, if you see TCP and UDP,

you know you're dealing with layer 4.

We also have things like WAN accelerators,

where we try to add compression to our IP packets,

and then we send those segments over

through those WAN accelerators

to get them through our network faster.

We also have load balancers and firewalls

that can operate at layer 4

by blocking and allowing different ports and protocols

to go through them.

For example, if you've ever gone in your firewall

and blocked a port like Port 80 over TCP,

well, that is a layer 4 block

because you're blocking the port, Port 80,

which is web traffic and the protocol TCP,

which is our protocol at layer 4.
