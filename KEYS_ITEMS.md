# Keys & Custom Items (test-only, not live)
Models: `nexus:key_{common,rare,steward,arena,lantern,moonlantern,starfall}` and `nexus:{arena_sigil,rift_dust,prism_shard,tyrant_core,nexus_spawner}`. Geyser: `geyser/nexus_keys_items.json`.

## Config changes needed later (NOT applied)
**ExcellentCrates `keys/*.yml`** - all 7 keys are `minecraft:tripwire_hook` with no model. Add an `item_model` component inside each `Value` NBT `components:{...}`:
`"minecraft:item_model":"nexus:key_common"` (common.yml), `key_rare` (rare.yml), `key_steward` (steward_key.yml), `key_arena` (arena.yml), `key_lantern` (lantern.yml), `key_moonlantern` (moonlantern.yml), `key_starfall` (vote.yml = Starfall).
Then `/excellentcrates reload` (plugin-level). Already-held keys keep their old NBT, so ExcellentCrates matching must still work. Test on one key first, because changing the NBT can break matching.
**NexusSkyblock** (needs a small code change in wt-061, since ItemMeta is built in code):
- ArenaEventService.summonItem -> `im.setItemModel(NamespacedKey("nexus","arena_sigil"))` (or config `summon.item-model`).
- RiftAltarService.mat -> per-mat `item-model:` in rift-altar.yml `mats.*` (rift_dust / prism_shard / tyrant_core). Tyrant Core shares HEART_OF_THE_SEA with the harvester placer, so the item_model is required, not CMD.
- Spawner items: set item_model `nexus:nexus_spawner` where tiered spawner items are built (SpawnerTierService), or leave vanilla.
item_model (1.21.4+) is preferred over custom_model_data: there's no base-item override, and Geyser v2 `definition` maps it 1:1.
