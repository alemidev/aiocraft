# aiocraft
**an asyncio-driven headless client library for block game with packet definitions**

aiocraft is a collection of types, definitions and utils to build minecraft clients without the official Java implementation

it is built on top of [PrismarineJS/minecraft-data](https://github.com/PrismarineJS/minecraft-data), which contains definitions for all types across all versions

aiocraft provides a raw implementation of a client but it isn't ready to be used, if you're looking for a convenient client library take a look at **[Treepuncher](https://git.alemi.dev/treepuncher/about)**

## Packets
the whole Minecraft protocol from `0.30c` to `1.19.3` is compiled and available
feature flags to only include certain protocol versions are planned
all types and packets are instantiable and serializable on all supported protocols:
```py
from aiocraft.proto.play.serverbound import PacketPosition

a_packet = PacketPosition(x=-4.0, y=64.0, z=10.5, onGround=True)
await client.dispatcher.write(a_packet)
```

## Client
an abstract client implementation is provided, but it's supposed to be extended (like in **[Treepuncher](https://git.alemi.dev/treepuncher/about)**)
the abstract client implements flows for all game phases and both a `.join()` or a `.info()` method to easily start the login flow

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
a chunk parser is provided with native code (Rust + PyO3). It is pretty fast but the abstract client doesn't make use of it

