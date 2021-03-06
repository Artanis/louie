=======
 About
=======

Louie is based on PyDispatcher_.  Here is a very good detailed
description of what both PyDispatcher and Louie offer you, based on
the description available at the PyDispatcher website.

.. _PyDispatcher: http://pydispatcher.sf.net/

PyDispatcher provides a multiple-producer-multiple-consumer
signal-registration and routing infrastructure, suitable for use in
multiple contexts.

The dispatcher mechanism is particularly useful when constructing
Model-View-Controller style applications where it is not desirable to
have the Model objects aware of the event model.

To be more concrete about what PyDispatcher does for you, here are
some specifics:

* A centralized service delivers messages to registered objects in the
  local process.  You can register any number of functions or other
  callable objects which can receive signals from senders.

  - Registration can be for any sender, particular sending objects, or
    "anonymous" messages (messages where the sender is None).

  - Registration can be for all signals, or particular signals.

  - A single signal will be delivered to all appropriate registered
    receivers, so that multiple registrations do not interfere with
    each other.

  - The sender or receiver need not be be dispatcher-aware.  Any
    Python object, except for `None`, can act as a sender, and any
    callable object can act as a receiver.

  - The system uses weak references to receivers wherever possible.

  - Object lifetimes are not affected by PyDispatcher registrations.
    When your object goes away, the registrations related to the
    object also go away.

  - References to common transient objects (instance methods in
    particular) are stored as compound weak references.

  - Weak references can be disabled on a registration-by-registration
    basis.

* It allows rich signal types. Signals must simply be hashable
  objects; they are otherwise opaque to the dispatch mechanism.

* Positional and keyword arguments may be attached to a signal when
  sending.  For each receiver, PyDispatcher sends each receiver the
  arguments that they expect; other arguments are silently dropped.
  Thus, receivers can be general in nature, even ignoring all
  arguments, or they can be specific, accepting whichever arguments it
  needs.
