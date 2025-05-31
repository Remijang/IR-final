# 7.1 Workload Assumptions  

Before getting into the range of possible policies, let us first make a number of simplifying assumptions about the processes running in the system, sometimes collectively called the workload. Determining the workload is a critical part of building policies, and the more you know about workload, the more fine-tuned your policy can be.  

The workload assumptions we make here are mostly unrealistic, but that is alright (for now), because we will relax them as we go, and eventually develop what we will refer to as ... (dramatic pause) ...  

a fully-operational scheduling discipline1.  

We will make the following assumptions about the processes, sometimes called jobs, that are running in the system:  

1. Each job runs for the same amount of time.   
2. All jobs arrive at the same time.   
3. Once started, each job runs to completion.   
4. All jobs only use the CPU (i.e., they perform no I/O)   
5. The run-time of each job is known.  

We said many of these assumptions were unrealistic, but just as some animals are more equal than others in Orwell’s Animal Farm [O45], some assumptions are more unrealistic than others in this chapter. In particular, it might bother you that the run-time of each job is known: this would make the scheduler omniscient, which, although it would be great (probably), is not likely to happen anytime soon.  

