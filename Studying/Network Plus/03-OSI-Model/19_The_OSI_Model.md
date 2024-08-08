In this lesson, I'm going to use a tool known as Wireshark,

which is a packet analyzer,

to be able to pull apart some network traffic

and show you the different layers of the OSI model.

Now, the actual usage of this tool known as Wireshark

is not covered by the Network+ exam.

You do need to know that this tool is a packet analyzer

and what kind of functions we might use it for.

And we'll talk about those specifically

in the troubleshooting section.

But for right now, I just want you to focus

on how I'm pulling apart these different layers

and the type of information I can get from Wireshark.

Again, this is going to be further and more in depth

than you need to know for the exam,

but it's going to help you understand

the OSI model a little bit better

as we start putting these pieces together from this theory

into something that's actually used on the network.

So let's jump into the environment and take a look.

All right, welcome to Wireshark.

Now, the first thing we need to do

is have a file to look at.

So I have a couple of different packet captures,

and I'm just going to open one up here,

and it's going to be right here.

This is an HTTP connection.

So what I'm showing here on the screen

is everything that happened for one computer

to make a request from my computer to a server and back.

So, as you can see here, it starts at time zero,

the source IP is my machine that sent the request,

and the destination IP is the server I'm trying to go to.

That's how we read these things.

It's time, source, destination,

the protocol used, in this case, TCP,

which we'll talk about later in the course,

and then the information that was sent.

As you go through,

you'll see there's this two-way conversation

going back and forth between the two,

and this is all at the packet layer.

And what you're seeing here is actually the session traffic

that was captured from one host to one server.

Now, as I scroll down a little bit further,

you're going to see it goes down

to 43 different line items happened.

It took 30 seconds total.

And we're going to go in and look at some of this information.

So let me go into this first packet.

And here, in the middle section,

you'll see that we have Frame 1. This was the first frame.

Now, going back to our OSI model, what is frame?

Where do frames operate?

Well, they operate at layer 2.

So I should expect to see some layer 2 data in here.

What type of things are layer 2 data?

Well, things like MAC addresses.

So if I open this up,

you're going to see that the encapsulation type was ethernet,

which is a layer 2 protocol.

We can see the time it arrived.

We can see the time that it left.

We can see what frame number it was

and how long the frame was.

We can see how much was captured,

and all that type of information there.

Next, if I go into Ethernet II,

this, again, is part of ethernet, which is layer 2,

and inside layer 2,

we can see our destination and our source.

So this is our destination.

This is the server I was trying to get to.

It's the MAC address.

And underneath it, we can see the source,

which is the machine that I had that made the request.

And it happened over IPv4.

And if I bring this down, you can actually see it

even further details.

Now, the next thing I'm going to look at is IPv4.

When we start talking about IP,

what are we talking about now?

We're talking about layer 3

because we're talking about Internet Protocol.

This means that we're going to have source and destination IPs,

as you can see here, highlighted in blue.

And if I open that up, you'll see that this was version 4,

we can see the header length,

and then we can actually dig into that packet.

But again, way beyond the scope of Network+.

The big thing we want to take away is,

layer 2 is MAC addresses, layer 3 was IPs.

Now, we go to layer 4, we're going to be talking about,

did we use TCP or UDP?

In this case, we used TCP.

So this is our layer 4 of the OSI model.

And as you can see, we're building up each of these layers

and all of that was one packet.

So the next one I'm going to do

is the one that came back from the server to the host.

So we sent the SYN over, and now we got back a SYN-ACK.

As we look at that, we can see the same type of information,

the same layout each time.

You'll see that we have our frame,

our layer 2 addresses, our IP addresses,

and then our TCP protocol layer 4.

So layer 2, layer 2, layer 3, layer 4.

And we can go through the entire packet

and look at each and every one of them.

Now, if I want to figure out what was happening

during this session, I can do that as well.

So if I go in here,

I can see that there was a GET request over HTTP.

Now, HTTP is a protocol. It's an application.

So this is actually a layer 7 capture here.

And what was done, if I open this up,

I can see that they went to the server etherreal.com,

they were using Mozilla, which is Firefox,

and that they came from this webpage,

etherreal.com/development.html,

and they clicked on the link for download.html.

And that's what we're asking for.

We're asking for the webpage, download.html at this point.

This then is acknowledged by the server

and goes back and forth

as we're getting more and more data.

And eventually, we get that webpage downloaded.

In fact, if I right-click on this,

I can tell it to follow the stream,

and I can see what that webpage looked like.

Now, this webpage is being shown to me in HTML

because that's how webpages are sent,

but this is exactly what this person got

when they went to that website,

and we captured all that in this network packet.

I could actually copy this, make it into an HTML file,

and then load it up inside of Internet Explorer,

or Edge, or Google Chrome, or Firefox

and be able to look at all of that.

So I think that's enough of that packet.

Let's take a look at another one

and see if it looks similar.

The next one I'm going to look at

is this one here that says FTP.

And what FTP is going to do is File Transfer Protocol.

It's going to be very similar.

You're going to see that we went from a source

to a destination, and then went back and forth

a whole bunch of different times.

And in this case, it was a much longer stream.

561 different packets went through that were captured.

So if I go back to the first one,

you'll see that there was this acknowledgement,

and they went back and forth,

and we can go through here and see frame.

Again, that's layer 2.

Ethernet.

And so again, we can see the source and the destination

as far as those MAC addresses.

If we go down to the next one, we go up to layer 3.

We're now seeing the source and destination IP addresses.

And when we get to layer 4,

we're able to see that this was a TCP session,

Transmission Control Protocol.

And so again, if I wanted to,

I can right-click this and follow that stream.

Now, when I follow that stream, what am I going to see?

I'm not going to see a pretty webpage

because this was FTP traffic.

Somebody was downloading a file.

All of this, if I convert it back

into its hexadecimal or binary format,

let's go to RAW, for instance,

I can copy this in and try to figure out

what type of file it was and put that back together.

That's what happens with network forensics

and digital forensics.

Way beyond the scope of this particular course,

but that's the idea here.

You can capture everything going over the network

into these PCAP files, packet capture files,

and you'll be able to open them inside of Wireshark

to see what type of traffic is being used on your network.

And as a network technician,

really, you're going to be focused mostly on this screen,

the source and the destination,

the protocol, and even the ports.

You can see here it went from port 80, the web port,

to port 2727.

The server then answered up from 2727 back to port 80,

and they went back and forth throughout this communication.

Let's open up one more. We're going to open up Telnet.

Now, Telnet is a way to remotely control a computer.

Again, you're going to see that we have the time,

the source, the destination, and the protocol,

just like we did before.

We have our SYN, SYN-ACK, ACK,

which is that three-way handshake.

And again, down here, we have layer 2, layer 2,

layer 3, and layer 4.

Now, in the protocol column, you're going to see TCP,

but you're also going to see this Telnet data.

And that is an application, so this is layer seven again,

just like we saw with HTTP before.

And if I go over here, I can see that layer 7 now is added,

and I get different information for that.

If I go through and right-click it and follow that stream,

let's see what we get this time.

There we go.

So what we're seeing is the person and their session

when they try to connect to a Telnet server.

So what you see in blue is what the server sent back.

So when they connected, the server said, "Hey,

"I'm an OpenBSD server, log in."

What the person did was they typed, F-A-K-E,

which you can see is red.

That's what the user sent to the server.

And the blue is what the server displayed on the screen,

which was F-A-K-E, so their username was fake.

Then, it asked for their password

and the user typed in, user.

So their username is fake and their password is user.

At this point, they were able to log into the server

and start running commands.

They ran the ls command,

which if you remember from A+, on a Unix system,

it's going to list the contents of a directory.

And then, they did it again, ls -a.

They wanted to see it going across the side.

And you saw, this is what came back.

This is the list of directories.

Then, they tried to run a program,

sbin/ping www.yahoo.com,

and that is showing that they tried to do a ping

from this Telnet server out to yahoo.com,

and they received this information back.

Now, we're seeing the entire conversation.

We're seeing both halves.

But if I wanted to see

just what one person sent to the other,

I can see the server side.

It's a lot easier to read, right?

But now, I don't see that password.

I don't see the commands that got sent over.

When I go here and I switched over to the client side,

this is what they typed in.

I can see that they typed in user, which was their password,

fake, which was their username,

and then the commands, the list command, the list all,

and the sbin/ping www.yahoo.com, and then exit.

So you can see how this is useful,

where we can start digging into this stuff.

If you go further in your career with CompTIA

and you go to your Cybersecurity Analyst training

or your PenTest+ training,

you'll get very familiar with Wireshark

and be able to dig in

and grab this information from the wire.

Now, again, like I said,

this video is a little bit beyond the scope

of what you need to know for the Network+ exam,

but hopefully, I've whetted your appetite,

where you're really interested in being able to learn more

about Wireshark and be able to learn how you can use this,

both as a network technician,

be able to see where the breakdown in communication is,

whether it's layer 2, layer 3, layer 4, or layer 7,

or using it more from the defense side,

with cybersecurity analysts going through these packets

and figuring out what did the bad guy do on your system,

because you'll be able to see what the bad guy did

because it's capturing everything,

both the server side and the client side,

or if you're using it for PenTest+,

if you got this type of data,

you now have access to that person's username and password

that you can use as a follow on in your pentest.

So I hope you enjoyed this video.

Now, let's get back to Network+.
