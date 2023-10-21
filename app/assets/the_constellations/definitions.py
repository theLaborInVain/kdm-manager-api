'''

    Dragon King expansion constellations are used to facilitate Survivor
    Sheet visuals.


'''


the_constellations = {
    "lookups": {
        "name": "The Constellations table lookups",
        "map": {
            "9 Understanding (max)": "A1",
            "Destined disorder": "B1",
            "Fated Blow fighting art": "C1",
            "Pristine ability": "D1",
            "Reincarnated surname": "A2",
            "Frozen Star secret fighting art": "B2",
            "Iridescent Hide ability": "C2",
            "Champion's Rite fighting art": "D2",
            "Scar": "A3",
            "Noble surname": "B3",
            "Weapon Mastery": "C3",
            "1+ Accuracy attribute": "D3",
            "Oracle's Eye ability": "A4",
            "Unbreakable fighting art": "B4",
            "3+ Strength attribute": "C4",
            "9 Courage (max)": "D4",
        },
        "formulae": {
            "Witch":    set(["A1","A2","A3","A4"]),
            "Rust":     set(["B1","B2","B3","B4"]),
            "Storm":    set(["C1","C2","C3","C4"]),
            "Reaper":   set(["D1","D2","D3","D4"]),
            "Gambler":  set(["A1","B1","C1","D1"]),
            "Absolute": set(["A2","B2","C2","D2"]),
            "Sculptor": set(["A3","B3","C3","D3"]),
            "Goblin":   set(["A4","B4","C4","D4"]),
        },
    },
}
