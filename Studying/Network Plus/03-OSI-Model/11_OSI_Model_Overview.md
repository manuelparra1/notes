The OSI model.

What is the OSI model?

Well, it stands for the Open Systems Interconnection model,

and it was developed all the way back in 1977

by the International Organization for Standardization.

This organization is responsible

for creating different standards,

which we refer to as the ISO.

And there's some number usually behind it.

For example, if you see ISO 7498,

that's the standard we use to refer to the OSI model.

Now for the exam,

you don't have to go

and worry about memorizing the ISO number,

but I did want to introduce you to this concept

because in everything we cover in computing,

there's some sort of standard associated with it.

Now, in the case of the Open Systems Interconnection model,

most people simply call this the OSI model,

but you may sometimes hear it referred to as the OSI stack.

Either way, we're talking about exactly the same thing here.

The OSI model is extremely important

to the network plus exam,

because it's a fundamental thing that we use to discuss

all the pieces and parts of a network.

It's so important,

that you're going to see a lot of questions

on the network plus exam about this concept

and how it relates to other things.

The OSI model is made up of seven different layers,

and we're going to talk about each of these seven layers

in the next seven videos covering one layer per video,

because this model is just that important

to understanding our networks.

Now, as we work through this section of the course,

we're going to be focused mainly on domain one,

networking fundamentals, specifically, objective 1.1,

which states that we must be able to compare and contrast

the Open Systems Interconnection or OSI model layers

and the encapsulation concepts.

We're also going to briefly jump into domain five,

network troubleshooting, towards the end of this section,

because I'm going to use a network tool called Wireshark

to help show you how we can break down the data

that's transferring over our networks

into various layers of the OSI model.

This tool, Wireshark,

is specifically listed under objective 5.3,

which states "given a scenario,

use the appropriate network software tools and commands".

Wireshark is a really helpful tool

that's used a lot in troubleshooting,

but even the OSI model itself can be helpful as a framework

to think through when you're doing your troubleshooting too.

These seven layers of the OSI model

are useful when you're trying to troubleshoot a network,

because if I have a problem and I can think about it

from all the different seven layers,

I can start to identify exactly where the problem is,

and then I can troubleshoot it appropriately.

This means the OSI model

can also serve as a reference model.

Now you may be wondering

what's the exact purpose of a reference model?

Well, a reference model is simply

something that we use to categorize

the functions of a network into a particular layer,

and that's what we're going to use the OSI model for

during our troubleshooting efforts.

Now, when you start looking at the OSI model in depth,

you're going to start to notice

that the OSI model doesn't actually cleanly

or easily or accurately refer to the way our modern networks

actually operate these days.

For example, some things are going to operate

at multiple layers of the OSI model,

especially when we're discussing the upper three layers.

Now there's a good reason

for why the OSI model isn't perfect

for our way that networks operate today.

And that's because our networks operate under a model

known as the TCP/IP model,

but the OSI model was designed

to refer to how all networks operate,

not just TCP/IP networks.

Now I know that may be a little bit confusing,

but don't worry too much about it yet.

It's going to make a lot more sense

as we go through the OSI model and the TCP/IP model.

After we talk about all seven layers of the OSI model,

we'll go back and compare the OSI model and the TCP/IP model

in the next section of this course,

and you'll see what I mean.

But to keep things simple for right now,

let's just remember that the OSI model is a reference model

and we're going to use it in our network operations

and troubleshooting because again,

it's generic in nature

and it's going to allow us to work for any

and all networks we may have.

Not just our most common networks, which are TCP/IP.

Now, one of the benefits of using a reference model

like the OSI model is that it can be used equivalently

across lots of different technologies

and a lot of different manufacturers as well.

So if I'm going to look at a particular

wireless network card from my computer,

I can compare how it operates

through the seven layers of the OSI model,

and then compare it equivalently to a different

manufacturer's card.

When you can understand the functions

at each and every layer that's being performed,

it's going to help you better understand

the flow of data in the network and through that card

and how it communicates and how you can troubleshoot it.

Now I've mentioned that there are seven layers

of the OSI model, several times in this video already,

but I still haven't even showed you what they are.

So let's take a look at the seven layers of the OSI model.

First, we start at the bottom layer

working our way from layer one,

all the way to the top layer, which is known as layer seven.

These are the physical layer, the data link layer,

the network layer, the transport layer, the session layer,

the presentation layer and the application layer.

For the exam, you need to be able to remember

these seven layers in the proper order

going from bottom to top and top to bottom.

Now, to help you with that, I like to use a memory aid

known as a pneumonic.

In the case of the OSI model,

I like to think about my favorite kind of pizza

when I'm listing things

from the bottom layer to the top layer.

Now my favorite kind of pizza is sausage pizza.

So if you want to remember these seven layers

of the OSI model, just remember what I always say

about sausage pizza.

Please do not throw sausage pizza away.

After all, I think sausage pizza is pretty tasty, right?

And so you shouldn't throw it away and waste it.

Now by using this sentence,

you can remember the seven layers from bottom to top.

Just take the letters from this sentence.

Please do not throw sausage pizza away, or P D N T S P A,

and replace it with the words, physical, data link, network,

transport, session, presentation, and application.

And there you have it, the seven layers of the OSI model.

Well, at least that's how I remember the seven layers

of the OSI model, but you can create your own pneumonic too.

I've heard several interesting ones over the years

from my students.

Once I was teaching this class of Navy Sailors

and they told me, they're saying was,

please do not tell shore patrol anything.

For those of you who don't know,

shore patrol is basically like the military police officers.

So I'm guessing they didn't want to get in trouble

with their ships captain so they said,

please don't tell shore patrol anything.

Now, another one of my students told me his pneumonic was,

please do not teach students pointless abbreviations,

which is kind of funny since the abbreviation

is what we're trying to remember here,

to remember the seven layers.

Whatever works for you is fine with me.

Just remember that you need to memorize these seven layers

before you take the exam, because on the exam,

you're going to get questions about these seven layers.

Now you might see some easy questions, like,

"what is the seventh layer of the OSI model?"

and then you'd pick out the word application.

Or they might say, "what layer is the session layer at?"

and you'll have to answer layer five.

Now you might also get some more complex things

asking you about a device

and figuring out what layer that device operates in.

For example, a router operates at layer three

or the network layer, but a hub is a physical device

and it operates at layer one, the physical layer.

Because of this, we're going to cover each

and every layer of the OSI model

in this section of the course,

so you can learn which devices are used there

and which protocols and other information like that.

All right, before we finish up this lesson,

we need to talk about one more thing, and that's data,

because networks are all about communicating data.

Well, we're going to specifically talk about

how data is going to be called different things

as it flows through our network

and as it goes through different names,

as it goes through those different layers of the OSI model.

Now, when we're talking about data,

we're actually talking about information

at layers five, six, and seven of the OSI model.

Now, as it moves down through the layers,

we're going to go from four to three to two to one,

and we're going to change its name each time.

When we're at layer four or the transport layer,

we're going to call data a segment.

When we go to layer three or the network layer,

we refer to it as a packet.

When we go into layer two or the data link layer,

we call it a frame.

And finally, when we're operating at layer one

or the physical layer,

this is where you've converted that data into ones and zeros

to send it across our medium, we call this bits.

Now this is something you need to memorize for the exam

as well, but don't worry,

I have another pneumonic to help you remember it.

This one is a simple question.

Do some people fear birthdays?

Now, I think that's a valid question

because as we get older,

sometimes people start fearing their birthday

because they don't want to age or appear older.

Now, again, I know this is silly,

but hopefully it helps you remember

the four types of information

as they flow through those lower layers.

So if you can remember, do some people fear birthdays,

that's going to give you D S P F B as your pneumonic.

Now, if we add our data types,

again, we always start with data

and then we had the other four layers,

we have data, segments, packets, frames, and bits.

So for the exam, it's really important

to understand the seven layers of the OSI model

and how data moves up and down through the layers

throughout the transmission process

and what those data types are going to be called.

So with that said,

let's jump into our lessons on the OSI model.
