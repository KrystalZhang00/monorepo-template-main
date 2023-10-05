**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: *Undoing Drawing Actions*

**Primary Actor**: *User*

**Goal in Context**: *The primary actor aims to undo their recent drawing actions on the canvas within the mini-paint program.*

**Preconditions**: * The mini-paint program is running, and the user is actively working on a canvas.*

**Trigger**: *User selects the "Undo" option.*
  
**Scenario**: *1. User is working on the canvas and realizes they made an undesired drawing action.
2. User accesses the program's menu or toolbar and selects the "Undo" option.
3. The system identifies the most recent drawing action to undo (e.g., the last stroke or change).
4. The system reverts the canvas to the state before the selected drawing action was performed.
5. User continues working on the canvas.*
 
**Exceptions**: *1. If the "Undo" action is not available (e.g., no recent actions to undo), the system should disable the option, and the user should continue without undoing.
2. System errors during the undo process should display an error message, and the user should attempt the action again.*

**Priority**: *High-priority.*

**When available**: *First release*

**Channel to actor**: *The primary actor (user) interacts with the system through the program's GUI, specifically by selecting the "Undo" option from the menu or toolbar.*

**Secondary Actor**: *N/A*

**Channels to Secondary Actors**: *N/A*

**Open Issues**: *Ensure the "Undo" functionality is responsive and can handle multiple levels of undo if needed for more complex drawings.*

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
