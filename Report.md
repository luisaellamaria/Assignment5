Assignment 5 
---------------------

# Team Members

- Emma Kozmmér
- Luisa Ella Mueller

# GitHub link to your (forked) repository

https://github.com/luisaellamaria/Assignment5.git


# Task 1

Note: Some questions require you to take screenshots. In that case, please join the screenshots and indicate in your answer which image refer to which screenshot.
1. What happens when Raft starts? Explain the process of electing a leader in the first term.

Ans:
- Leader election: First of all, when Raft starts, all nodes start as followers and wait for messages (heartbeats) from a leader. If followers don't hear from a leader within a certain timeframe (election timeout) it is clear that no leader exists. Therefore, the current node is supposed to change to a candidate and start a new election term. The candidate requests votes from other nodes. Nodes will reply with their vote based on criteria like completeness of the candidate’s log and whether they have voted in that term. The candidate becomes the leader if it gets votes from a majority of nodes. Once the leader is elected, all changes to the system now go through the leader (it starts sending heartbeats) to maintain authority and prevent new elections.

Note: we got this information from the link which was provided to us: https://thesecretlivesofdata.com/raft/ there we followed the step by step explanation of each step in the election process.


2. Perform one request on the leader, wait until the leader is committed by all servers. Pause the simulation. Then perform a new request on the leader. Take a screenshot, stop the leader and then resume the simulation. Once, there is a new leader, perform a new request and then resume the previous leader. Once, this new request is committed by all servers, pause the simulation and take a screenshot. Explain what happened?

Ans: 
- First of all, we performed a request on the existing leader (S1) and the leader (S1) replicated the entry to the other nodes. The entry was committed once a majority of nodes have written it to their logs, represented by the solid borders around the  first logs (which are for all nodes a 2).  The simulation was then paused and a new request on the same leader (S1) was performed. Then, we paused the simulation and performed a new request on the leader.  Since it was not defined to wait in the instruction we immediately took a screenshot (./image-folder/task1_qq2_1.png)(task1_q2_1.png (also provided in our images folder)). On the screenshot there is one column where all logs are surrounded by solid borders, indicating that replication has been completed and the entries has been committed by all nodes. In the second column only the leader log is surrounded by a solid column and the other logs are surrounded by dotted boarders, indicating that the leader was not committed by the servers yet but if we run the simulation further we will get also those solid boarders like for the first column.
- Further, we stopped the leader and resumed the simulation. We performed a new request on the new leader and paused the simulation once the request was committed by all servers. The result of this process can be seen in our second screenshot (task1_q2_2.png (also provided in our images folder)).  In the screenshot we can inspect that due to the stop of the first leader (S1) a new leader (S3) was selected in a new term. Since the previous leader (S1) was then resumed, the new leader (S4) was able to be committed by all other nodes (including the previous leader). This commitment can be seen by the solid boarders around all the third logs of all (green) nodes. 

=> The whole process illustrated how the Raft algorithm handles leader failures maintaining integrity and consistency. When a leader fails (is stopped), the remaining nodes can conduct a new leader election.


3. Stop the current leader and two other servers. After a few increase in the Raft term, pause the simulation and take a screenshot. Then resume all servers and restart the simulation. After the leader election, pause the simulation and take a screenshot. Explain what happened.

Ans:
- After we let the two servers running during a few term increments, we observed a behavioural pattern. The terms kept increasing  (as nodes continually attempt to elect a leader) but no new leader can be elected, because in Raft a majority of nodes is required to make decisions.  Hence, the process was kind of stuck, leading to no solid border around any new entries in the logs, indicating no new leader has been elected and no new entries have been committed.  This can be seen in the screenshot (task1_q3_1.png (also provided in our images folder)).   
- Once al the servers were resumed, they were able to communicate again and hold a new leader election. So, node S5 was chosen as the new leader. The screenshot for this part shows a new term with a leader elected (indicated by the number in a circle on one of the servers)  (task1_q3_2.png (also provided in our images folder)). If a new request was performed on the new leader the entries would be replicated and committed. 

=> The whole process illustrated the Raft algorithm's requirement for a majority of nodes to be operational to maintain the system's reliability and functionality.


# Task 2

Indicate the replies that you get from the "/admin/status" endpoint of the HTTP service for each servers. Which server is the leader? Can there be multiple leaders?

Ans: We got the following replies from the "/admin/status" endpoint of the HTTP service for each servers:

- Request 1: http://localhost:8080/admin/status: 
{'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6000'), 'state': 2, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 6, 'commit_idx': 6, 'raft_term': 1, 'next_node_idx_count': 2, 'next_node_idx_server_127.0.0.1:6001': 7, 'next_node_idx_server_127.0.0.1:6002': 7, 'match_idx_count': 2, 'match_idx_server_127.0.0.1:6001': 6, 'match_idx_server_127.0.0.1:6002': 6, 'leader_commit_idx': 6, 'uptime': 605, 'self_code_version': 0, 'enabled_code_version': 0}

- Request 2: http://localhost:8081/admin/status:
{'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6001'), 'state': 0, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'partner_node_status_server_127.0.0.1:6002': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 6, 'commit_idx': 6, 'raft_term': 1, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 6, 'uptime': 624, 'self_code_version': 0, 'enabled_code_version': 0}

- Request 3: http://localhost:8082/admin/status:
{'version': '0.3.12', 'revision': 'deprecated', 'self': TCPNode('127.0.0.1:6002'), 'state': 0, 'leader': TCPNode('127.0.0.1:6000'), 'has_quorum': True, 'partner_nodes_count': 2, 'partner_node_status_server_127.0.0.1:6001': 2, 'partner_node_status_server_127.0.0.1:6000': 2, 'readonly_nodes_count': 0, 'log_len': 2, 'last_applied': 6, 'commit_idx': 6, 'raft_term': 1, 'next_node_idx_count': 0, 'match_idx_count': 0, 'leader_commit_idx': 6, 'uptime': 636, 'self_code_version': 0, 'enabled_code_version': 0}

- From this responses we can read in every response that 'leader': TCPNode('127.0.0.1:6000‘). Therefore server 0 at the port 8080 is our leader.

- Since this is the Raft algorithm it is not possible to have multiple leaders.

2. Perform a Put request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?
Ans:
Status: 200
Changes:


4. Perform an Append request for the key ``a" on the leader. What is the new status? What changes occurred and why (if any)?
Ans:
Status: 200
Changes:

5. Perform a Get request for the key ``a" on the leader. What is the new status? What change (if any) happened and why?
Ans:
Status: 200
Changes:


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

What is a consensus algorithm: 

A consensus algorithm is a process used to achieve agreement on a single data value among distributed processes or systems. Consunsus Algorithms have been designed to coordinate the system's processes to agree on data value and how that will be used in the system. 
It ensures that network activities are done in a secure and reliable manner which establishes trust among peers in the network.

A replicated state machine is a deterministic state machine where multiple machines have the same state and run the same. 

 What are they used for in the context of replicated state machines? 

They are important in distributed systems to ensure that each node maintains an identical copy of a particular state. 

It is important to coordinate updates: 

When changes to the state are required (like a new transaction in a distributed ledger), all nodes must agree on the order and content of these changes. A consensus algorithm ensures that all nodes agree on the sequence of actions that modify the state. 

Handling failures: 

In distributed systems, nodes can fail, become unresponsive, or even act maliciously. Consensus algorithms are designed to handle these issues by ensuring that the overall system continues to operate correctly and agree on the state, even if some nodes are not functioning properly.


2. What are the main features of the Raft algorithm? How does Raft enable fault tolerance?

Ans: 

Raft uses a well-defined leader election process. When the current leader fails or becomes unreachable, a new leader is elected, ensuring continuous coordination among nodes.


The leader is responsible for log replication. All changes to the state are first made on the leader's log, then replicated to the follower nodes, ensuring consistency across the cluster.

Raft ensures that if any node has applied a particular log entry to its state machine, then other nodes won't apply a different command for the same log index. This guarantees consistency across the system.

Raft forces the logs of the followers to match those of the leader. If a follower's log diverges, the leader overwrites it with its own data, ensuring all nodes maintain identical logs.

Before a leader can consider a log entry as committed, it must first store entries from previous leaders. This ensures data consistency across leader changes.



3. What are Byzantine failures? Can Raft handle them?

Ans: 
<<<<<<< HEAD

What are Byzantine failures?

Byzantine failures, named after the Byzantine Generals' Problem, represent one of the most challenging class of failures in distributed systems. They describe a situation where components of a system fail in arbitrary or unpredictable and malicious ways, which can include disinformation, sending conflicting information to different parts of the system, or working to actively undermine the system's operation. This is different from standard failures where a component simply stops working or responds with an error.

Can Raft handle them?

No, Raft's initial description is not byzantine fault-tolerant.

If a node that votes two times in a given term, or votes for some node that has an information which is not updated and that node becomes leader. Such behaviour could cause inconsistencies in the log or could lead to two nodes that both believe themselves to be leaders.

In order to make the Raft Byzantine fault tolerant, there must be many significant changes to the algorithm.

However, after doing some research, we have an interesting paper which  describes how one could make it fault tolerant: https://www.scs.stanford.edu/17au-cs244b/labs/projects/clow_jiang.pdf

