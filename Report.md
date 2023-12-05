Assignment 5 
---------------------

# Team Members

- Emma Kozmmér
- Luisa Ella Mueller

# GitHub link to your (forked) repository

...

# Task 1

Note: Some questions require you to take screenshots. In that case, please join the screenshots and indicate in your answer which image refer to which screenshot.
1. What happens when Raft starts? Explain the process of electing a leader in the first term.
Ans:
- Leader election: First of all, when Raft starts, all nodes start as followers and wait for messages (heartbeats) from a leader. If followers don't hear from a leader within a certain timeframe (election timeout) it is clear that no leader exists. Therefore, the current node is supposed to change to a candidate and start a new election term. The candidate requests votes from other nodes. Nodes will reply with their vote based on criteria like completeness of the candidate’s log and whether they have voted in that term. The candidate becomes the leader if it gets votes from a majority of nodes. Once the leader is elected, all changes to the system now go through the leader (it starts sending heartbeats) to maintain authority and prevent new elections.

Note: we got this information from the link which was provided to us: https://thesecretlivesofdata.com/raft/ there we followed the step by step explanation of each step in the election process


2. Perform one request on the leader, wait until the leader is committed by all servers. Pause the simulation. Then perform a new request on the leader. Take a screenshot, stop the leader and then resume the simulation. Once, there is a new leader, perform a new request and then resume the previous leader. Once, this new request is committed by all servers, pause the simulation and take a screenshot. Explain what happened?
Ans: 
In this final screenshot, the logs of the nodes show several committed operations (indicated by the filled circles with a triangle). The fact that each server has the same number of committed entries suggests that the cluster has reached consensus on these entries.
Based on the series of steps you've provided, here's what happened during the exercise:
* 		A leader was elected and began to replicate its log entries to the follower nodes.
* 		A request was sent to the leader, which was then replicated and committed across all nodes. This state was captured in your first screenshot.
* 		The simulation was paused, and a new request was sent to the leader, after which a screenshot was taken.
* 		The leader was then stopped, simulating a leader failure, and the simulation was resumed to trigger a new election.
* 		A new leader was elected, which is evident from the term increment to '2' on all nodes and the replication arrows from S5, which indicate it's the current leader.
* 		Another request was sent to the new leader, which was replicated and committed across all servers.
* 		The leader from the previous term was resumed, and at this point, the new request was already committed by all servers. The simulation was paused again, and another screenshot was taken.
During the process:
* The term number increased, which means an election occurred and a new term was started.
* The logs show multiple committed entries, reflecting the operations that were sent to the leader.
* All servers, including the previously stopped leader, updated their logs to reflect the new committed entries, ensuring consistency across the cluster.
This exercise demonstrated how the Raft consensus algorithm ensures that a distributed system continues to operate smoothly even in the event of a leader failure. When a new leader takes over, it proposes its new log entries, which are then replicated to the followers. When the old leader rejoins the cluster, it adopts the updated log from the current leader to maintain consistency. This is how the Raft algorithm maintains a consistent state across the cluster, with a new leader stepping in and the old leader syncing up when it rejoins.


3. Stop the current leader and two other servers. After a few increase in the Raft term, pause the simulation and take a screenshot. Then resume all servers and restart the simulation. After the leader election, pause the simulation and take a screenshot. Explain what happened.
Ans:





# Task 2

Indicate the replies that you get from the "/admin/status" endpoint of the HTTP service for each servers. Which server is the leader? Can there be multiple leaders?
Ans: 
Ans:

Perform an Append request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?

Ans: 

Perform a Get request for the key ``a" on the leader. What is the new status? What change (if any) happened and why?

Ans:



# Task 3

Shut down the server that acts as a leader. Report the status that you get from the servers that remain active after shutting down the leader.

Ans:

 Perform a Put request for the key "a". Then, restart the server from the previous point, and indicate the new status for the three servers. Indicate the result of a Get request for the key ``a" to the previous leader.

Ans:

Has the Put request been replicated? Indicate which steps lead to a new election and which ones do not. Justify your answer using the statuses returned by the servers.

Ans:

Shut down two servers, including the leader --- starting with the server that is not the leader. Report the status of the remaining servers and explain what happened.

Ans:

Can you perform Get, Put, or Append requests in this system state? Justify your answer.

Ans:

Restart the servers and note down the new status. Describe what happened.

Ans:




# Task 4

1. What is a consensus algorithm? What are they used for in the context of replicated state machines? 

Ans: 

2. What is a consensus algorithm? What are they used for in the context of replicated state machines? 

Ans: 


3. What are Byzantine failures? Can Raft handle them?

Ans: 
