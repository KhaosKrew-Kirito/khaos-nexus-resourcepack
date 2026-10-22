# Batch 3 (improved) - replaces batch 2 versions of these ids
3D multi-element models (Blockbench-style JSON, 64x64 atlas, hand-shaded ramps with edge highlights, `light_emission: 15` on glow parts, display transforms for gui/hand/head):
ember_blade, frostbloom_blade (now "Soulfrost Blade"), rift_scythe (upgraded from v1 flat), starforge_pickaxe, starry_hat, cozy_witch_hat, candy_corn_saber, rift_altar (block), harvester_mining (block).
Bedrock: icons are the 3D renders (64px); 3D Bedrock geometry/attachables still TODO. Generator: tools/gen_batch3.py.
Still batch-2 quality (to redo): grove_axe, starlit_shovel, moonlure_rod, aurora_bow, harvester_farming/fishing/essence, autosell_chest, hearth_beacon, 7 decor blocks.

# Batch 2 skins + custom block skins (STAGED, NOT LIVE)
Do not publish a release from this branch until the owner OKs; live pack sha1 a96afafc... unchanged.
## Item skins (pack/assets/nexus/items/<id>.json -> item_model nexus:<id>)
| id | name | base items | drops from |
|---|---|---|---|
| ember_blade | Ember Blade | swords | Moonlantern Crate |
| frostbloom_blade | Frostbloom Blade | swords | Moonlantern Crate |
| starforge_pickaxe | Starforge Pickaxe | pickaxes | Moonlantern Crate |
| grove_axe | Grovewarden Axe | axes | Moonlantern Crate |
| starlit_shovel | Starlit Shovel | shovels | Moonlantern Crate |
| moonlure_rod | Moonlure Rod | fishing_rod | Moonlantern Crate |
| aurora_bow | Aurora Bow | bow | Moonlantern Crate |
| starry_hat | Starry Wizard Hat | hat (paper + equippable head) | Moonlantern Crate |
| candy_corn_saber | Candy Corn Saber | swords | Lantern Chest (Halloween) |
| cozy_witch_hat | Cozy Witch Hat | hat | Harvest Stand (Halloween) |
## Custom block skins (models/block/<id>.json, cube_bottom_top)
harvester_mining, harvester_farming, harvester_fishing, harvester_essence, rift_altar, autosell_chest, hearth_beacon,
Nexus Decor: ember_lantern, moon_lamp, rift_crystal, starfall_stone, wisp_jar, harvest_bale, glow_mushroom.
Display via item_display entity / item_model over the vanilla base block (Bedrock sees the vanilla base, per CustomBlockService).
## Bedrock
geyser/nexus_skins_batch2.json (merge into custom_mappings), bedrock/textures/items + item_texture_batch2.json (merge into mcpack).
Hat and block 3D attachables are still TODO for Bedrock (these show as flat icons).
## Plugin TODO
Wardrobe: add the ids to wardrobe.yml as `skin:` entries (`/wardrobe skin <id>` for tools, and hat `model:` for hats); crate rewards grant nexus.wardrobe.<id>.
