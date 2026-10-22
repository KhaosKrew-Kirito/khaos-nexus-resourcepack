KHAOS NEXUS - RESOURCE-PACK SKINS (Phase 1 prototype, 0.9.0-test)  - NOT INSTALLED, NOTHING LIVE
=====================================================================================
PIPELINE
 Java : 1.21.4+ item definitions (item_model component) + equipment assets (armor). Pack format 75 (MC 1.21.11).
 Bedrock: Geyser v2 custom item mappings (custom_mappings/nexus_skins.json) + KhaosNexus-skins.mcpack
          (item textures + attachables for hat/armor). Same Java item_model key drives both.
 Plugin: wardrobe.yml `resource-pack-skins: false` (default). When true:
   - hats with `model:` -> PAPER + item_model + head equippable (packet overlay, as today)
   - armor with `equipment:` -> IRON_* pieces with item_model nexus:<set>_<slot> + equipment asset (packet overlay)
   - /wardrobe skin <id> | /wardrobe skin off : sets/clears item_model on the held sword only. Stats, enchants,
     name untouched. Skin id stored in item PDC (nexusskyblock:weapon_skin). Owned via nexus.wardrobe.<id>.
   Test-gated as before (owner only).

FILES
 NexusSkyblock-0.9.0-test.jar       plugin (incl. 0.8.x work; 110 tests pass)
 KhaosNexus-skins-java.zip          Java pack  sha1 a96afafca8a0c5b37118e1606f53856962c408cb
 KhaosNexus-skins.mcpack            Bedrock pack sha1 fbfc79ee8fecc5c0d7618223bbf431a9c7b02f64
 nexus_skins.json                   Geyser mapping -> plugins/Geyser-Spigot/custom_mappings/
 blockbench/                        .bbmodel sources (pumpkin_head, harvester) + PNGs
 previews/                          renders

HOSTING (Java pack needs a public HTTPS URL + sha1)
 Recommended (free): GitHub release asset on a public repo, e.g.
   https://github.com/<owner>/khaosnexus-pack/releases/download/v1/KhaosNexus-skins-java.zip
 Alternatives: Cloudflare R2/Pages (free tier). Avoid Dropbox/Drive (redirects break clients).
 server.properties lines to set AT INSTALL TIME (not changed yet):
   resource-pack=<url>
   resource-pack-sha1=a96afafca8a0c5b37118e1606f53856962c408cb
   require-resource-pack=false   (or true once tested)
   resource-pack-prompt={"text":"Khaos Nexus skins pack"}
 Every pack change = new zip, new sha1, new release tag (URL change avoids client caching).

INSTALL (needs owner OK - RESTART REQUIRED)
 1. Upload java zip to host, verify URL downloads, sha1 matches.
 2. Copy KhaosNexus-skins.mcpack -> plugins/Geyser-Spigot/packs/
 3. Copy nexus_skins.json -> plugins/Geyser-Spigot/custom_mappings/
 4. Replace plugins/NexusSkyblock jar with 0.9.0-test.
 5. Set server.properties lines above.
 6. Restart (Geyser loads packs/mappings only at startup; server.properties too).
 7. Owner test (Java + Bedrock): /wardrobe use riftwalker, /wardrobe use pumpkin_hat, hold sword -> /wardrobe skin rift_scythe, /wardrobe skin off.
 8. Then set wardrobe.yml resource-pack-skins: true + /wardrobe reload (plugin reload only, no /reload).

ROLLBACK
 resource-pack-skins: false + /wardrobe reload (instant, no restart; looks revert to dyed/trimmed).
 Full: remove mcpack + nexus_skins.json, clear resource-pack lines, restore 0.8.1-test jar, restart.
 Skinned swords left over just keep the model key; without the pack Java shows a missing-texture fallback,
 so run /wardrobe skin off on them or keep the pack.

CAVEATS
 - Requires Java 1.21.4+ clients for item_model; ViaBackwards clients (<1.21.4) see the base sword/iron armor.
 - Geyser: one mapping per base item+model (scythe mapped on all 6 swords). Mapped wearables must be max_stack 1.
 - Bedrock armor = attachables using vanilla armor geometry (64x32 layers); no custom armor shapes beyond that
   on Bedrock without custom geometry per piece. Hats can be any geometry (bone parented to head).
 - Bedrock item icons only change for mapped items; enchant glint ok.
 - Geyser custom item mapping keys on item_model, so skin changes need no plugin restart, but new skins
   (new mapping/mcpack entries) need a restart.

CUSTOM BLOCKS (Harvesters, Rift Altar, Nexus Decor) - documented, prototype = harvester model/textures only
 Approach: Java note_block blockstate overrides (instrument/note/powered = ~800 states) in the pack +
   Geyser custom block mappings (custom_mappings block section, java state -> bedrock custom block w/ geometry
   & material instances). Plugin must cancel note-block state updates (NotePlayEvent, physics) for used states
   and place/break custom items. Mushroom-stem states are a fallback.
 Not chosen: item_display entities - Geyser does NOT render display entities to Bedrock.
 Effort: ~1 day for the block framework, then ~30 min per simple cube block, 1-2 h per shaped model (altar).

EFFORT PER ADDITIONAL SKIN (programmatic art)
 weapon/hat ~15-30 min, armor set ~30-60 min, + pack rebuild + restart to ship (batch them).
