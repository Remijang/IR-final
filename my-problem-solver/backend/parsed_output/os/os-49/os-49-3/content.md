# 49.3 Focus: Simple And Fast Server Crash Recovery  

In this chapter, we will discuss the classic NFS protocol (version 2, a.k.a. NFSv2), which was the standard for many years; small changes were made in moving to NFSv3, and larger-scale protocol changes were made in moving to NFSv4. However, NFSv2 is both wonderful and frustrating and thus serves as our focus.  

In NFSv2, the main goal in the design of the protocol was simple and fast server crash recovery. In a multiple-client, single-server environment, this goal makes a great deal of sense; any minute that the server is down (or unavailable) makes all the client machines (and their users) unhappy and unproductive. Thus, as the server goes, so goes the entire system.  

