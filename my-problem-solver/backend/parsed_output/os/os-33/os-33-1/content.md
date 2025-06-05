# 33.1 The Basic Idea: An Event Loop  

The basic approach we’ll use, as stated above, is called event-based concurrency. The approach is quite simple: you simply wait for something (i.e., an “event”) to occur; when it does, you check what type of event it is and do the small amount of work it requires (which may include issuing I/O requests, or scheduling other events for future handling, etc.). That’s it!  

Before getting into the details, let’s first examine what a canonical event-based server looks like. Such applications are based around a simple construct known as the event loop. Pseudocode for an event loop looks like this:  

while (1) { events $\mathbf { \Sigma } = \mathbf { \Sigma }$ getEvents(); for (e in events) processEvent(e);   
}  

It’s really that simple. The main loop simply waits for something to do (by calling getEvents() in the code above) and then, for each event returned, processes them, one at a time; the code that processes each event is known as an event handler. Importantly, when a handler processes an event, it is the only activity taking place in the system; thus, deciding which event to handle next is equivalent to scheduling. This explicit control over scheduling is one of the fundamental advantages of the eventbased approach.  

But this discussion leaves us with a bigger question: how exactly does an event-based server determine which events are taking place, in particular with regards to network and disk I/O? Specifically, how can an event server tell if a message has arrived for it?  

