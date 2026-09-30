---
name: hardware-connection-check
description: Confirm debugger, emulator, board, or peripheral connections, power, and known interfaces with the user before targeted checks in hardware, embedded, or firmware tasks. Does not apply to code work that needs no device connection.
---

# Hardware Connection Check

Use the user's confirmation as the first source of connection information. Avoid first enumerating ports, searching for drivers, or repeatedly attempting connections.

## Confirmation order

1. Reuse any current connection status, device model, or port information the user has already supplied. Do not ask again.
2. Before initial enumeration, connection, or expanding checks after a connection failure, combine missing essential details into one short question: whether the emulator or debugger is connected to the computer and target board, whether the board is powered, whether relevant peripherals are connected, and any known interface or port. Ask only what the current task needs.
3. If the user confirms that hardware is disconnected or unpowered, state exactly what needs connecting, plugging in, powering, or selecting. Wait for completion before checking the device.
4. Once the user confirms readiness, perform the smallest necessary check using the known device, interface, or port. If it still fails, request the specific status or error before expanding checks based on evidence. Avoid blindly scanning all ports, reinstalling drivers, or retrying connections repeatedly.
5. While waiting for confirmation, continue independent work such as reading documentation or analyzing code. Do not treat an unconfirmed state as connected, or report assumptions or simulation results as verification on physical hardware.

## Boundaries

- Connection confirmation does not itself authorize flashing, erasing, resetting, restarting, or disconnecting a device. Use the user's current task and existing authorization to determine subsequent actions.
- Do not interrupt a running test to confirm connections. Record status the user has already given unless they explicitly request an action or there is a credible risk of hardware damage.
- Do not ask the user to repeat information already available in supplied logs or configuration.

Example:

> Before connecting, please confirm whether the debugger is connected to both the computer and target board, and whether the board is powered. Include the debugger model or serial port if known. I will continue the code checks that do not depend on the device.
