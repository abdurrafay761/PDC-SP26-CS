Chapter 2 

Topic: Barrier.py

What I Learned
Barrier makes threads wait until all reach a point.

How to Execute
python Barrier.py

Use / Output
Threads wait and continue together.

When to Use
When tasks must synchronize.

Advantages
Good coordination

Disadvantages
Slow if one thread delays

Summary
Barrier synchronizes threads.

Topic: condition.py

What I Learned
Threads wait and notify using condition.

How to Execute
python condition.py

Use / Output
Producer and consumer work together.

When to Use
Shared resources.

Advantages
Efficient communication

Disadvantages
Complex

Summary
Condition manages thread communication.

Topic: event.py

What I Learned
Event signals between threads.

How to Execute
python event.py

Use / Output
Producer signals consumer.

When to Use
Simple signaling.

Advantages
Easy

Disadvantages
Limited control

Summary
Event allows signaling between threads.

Topic: mythreadclass.py

What I Learned
Threads created using class.

How to Execute
python mythreadclass.py

Use / Output
Runs multiple threads.

When to Use
Custom behavior.

Advantages
Flexible

Disadvantages
Needs management

Summary
Custom threads provide control.

Topic: mythreadclasslock.py

What I Learned
Lock prevents simultaneous access.

How to Execute
python mythreadclasslock.py

Use / Output
One thread runs at a time.

When to Use
Shared data.

Advantages
Prevents errors

Disadvantages
Slower

Summary
Lock ensures safe execution.

Topic: mythreadclasslock2.py

What I Learned
Lock applied only to part of code.

How to Execute
python mythreadclasslock2.py

Use / Output
Better concurrency.

When to Use
Partial protection.

Advantages
Better performance

Disadvantages
Needs care

Summary
Selective locking improves speed.

Topic: rlock.py

What I Learned
Same thread can acquire lock multiple times.

How to Execute
python rlock.py

Use / Output
Safe add/remove operations.

When to Use
Nested locking.

Advantages
Prevents deadlock

Disadvantages
Slight overhead

Summary
RLock allows repeated locking.

Topic: semaphore.py

What I Learned
Controls access using counter.

How to Execute
python semaphore.py

Use / Output
Limits resource access.

When to Use
Limited resources.

Advantages
Controls concurrency

Disadvantages
Complex

Summary
Semaphore manages access.

Topic: threaddefinition.py

What I Learned
Basic thread creation.

How to Execute
python threaddefinition.py

Use / Output
Runs multiple threads.

When to Use
Simple tasks.

Advantages
Easy

Disadvantages
Limited

Summary
Basic threading runs tasks in parallel.

Topic: threaddetermine.py

What I Learned
Threads run independently.

How to Execute
python threaddetermine.py

Use / Output
Shows execution flow.

When to Use
Understanding threads.

Advantages
Clear concept

Disadvantages
Unpredictable order

Summary
Threads execute independently.

Topic: threadnameandprocesses.py

What I Learned
Threads can have names.

How to Execute
python threadnameandprocesses.py

Use / Output
Displays thread names.

When to Use
Debugging.

Advantages
Readable

Disadvantages
None

Summary
Naming helps identify threads.

Topic: threadingwithqueue.py

What I Learned
Queue helps safe communication.

How to Execute
python threadingwithqueue.py

Use / Output
Producer adds, consumer removes.

When to Use
Data sharing.

Advantages
Thread-safe

Disadvantages
Overhead

Summary
Queue enables safe communication.
