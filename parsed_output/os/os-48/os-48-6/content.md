# 48.6 Summary  

We have seen the introduction of a new topic, distributed systems, and its major issue: how to handle failure which is now a commonplace event. As they say inside of Google, when you have just your desktop machine, failure is rare; when you’re in a data center with thousands of machines, failure is happening all the time. The key to any distributed system is how you deal with that failure.  

We have also seen that communication forms the heart of any distributed system. A common abstraction of that communication is found in remote procedure call (RPC), which enables clients to make remote calls on servers; the RPC package handles all of the gory details, including timeout/retry and acknowledgment, in order to deliver a service that closely mirrors a local procedure call.  

The best way to really understand an RPC package is of course to use one yourself. Sun’s RPC system, using the stub compiler rpcgen, is an older one; Google’s gRPC and Apache Thrift are modern takes on the same. Try one out, and see what all the fuss is about.  

OPERATINGSYSTEMS[VERSION 1.10]  

