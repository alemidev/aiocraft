# aiocraft
**an asyncio-driven headless client library for block game with packet definitions**

aiocraft is a collection of types, definitions and utils to build minecraft clients without involving the official client and Java

it is built on top of [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data), which contains definitions for all types across all versions.

aiocraft provides a raw implementation of a client but it isn't ready to be used, if you're looking for a convenient client library take a look at **[Treepuncher](https://git.alemi.dev/treepuncher/about)**

## Packets
The whole Minecraft protocol from `0.30c` to `1.19.3` is compiled and available.
Feature flags to only include certain protocol versions are planned.
All types and packets are instantiable and serializable on all supported protocols:
```
from aiocraft.proto import PacketArmAnimation
a_packet = PacketArmAnimation(hand=0)
await client.dispatcher.write(a_packet)
```

## Client
An abstract client is provided, but it's supposed to be extended (like in **[Treepuncher](https://git.alemi.dev/treepuncher/about)**)
Such client includes all game phases implemented and both a `.join()` or a `.info()` method to handle the flow.

## Types
aiocraft defines these minecraft types:

 * `Dimension`
 * `Difficulty`
 * `Gamemode`
 * `GameProfile`
 * `Enchantment`
 * `BlockPos`
 * `Item` (without constants)
 * `Texture`
 * `Player`

more types are planned but still not generated:

 * `Entity`
 * `Block`
 * `Item` (with constants)

## World
A chunk parser is provided with native code (Rust + PyO3). It is pretty fast but the abstract client doesn't make use of it.

