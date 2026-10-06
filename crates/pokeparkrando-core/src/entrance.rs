#[derive(Clone, Copy, Debug, Eq, PartialEq)]
pub(crate) struct ZoneData {
    pub(crate) zone: i32,
    pub(crate) area: i32,
    pub(crate) position: i32,
}

macro_rules! entrance_zone_data {
    ($($name:ident = $exit:literal => ($zone:literal, $area:literal, $position:literal);)+) => {
        pub(crate) fn config_prefix(entrance: &str) -> Option<&'static str> {
            match entrance {
                $($exit => Some(stringify!($name)),)+
                _ => None,
            }
        }

        pub(crate) fn zone_data(exit: &str) -> Option<ZoneData> {
            match exit {
                $($exit => Some(ZoneData {
                    zone: $zone,
                    area: $area,
                    position: $position,
                }),)+
                _ => None,
            }
        }
    };
}

entrance_zone_data! {
    TREEHOUSE_MEADOW_PASSAGE_MEADOW_ZONE_CONNECTION = "Treehouse Meadow Passage - Meadow Zone Connection" => (2, 1, 0);
    MEADOW_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION = "Meadow Zone Main Area - Treehouse Connection" => (1, 1, 1);
    MEADOW_ZONE_VENUSAUR_AREA_MEADOW_ZONE_MAIN_GATE = "Meadow Zone Venusaur Area - Meadow Zone Main Gate" => (1, 2, 0);
    MEADOW_ZONE_MAIN_AREA_VENUSAUR_GATE = "Meadow Zone Main Area - Venusaur Gate" => (1, 1, 2);
    MEADOW_ZONE_MAIN_AREA_POKEPARK_ENTRANCE_GATE = "Meadow Zone Main Area - Pokepark Entrance Gate" => (1, 1, 0);
    POKEPARK_ENTRANCE_MEADOW_ZONE_GATE = "Pokepark Entrance - Meadow Zone Gate" => (99, 1, 1);
    BEACH_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION = "Beach Zone Main Area - Treehouse Connection" => (3, 1, 0);
    TREEHOUSE_BEACH_PASSAGE_BEACH_ZONE_CONNECTION = "Treehouse Beach Passage - Beach Zone Connection" => (2, 1, 1);
    ICE_ZONE_MAIN_AREA_ICE_ZONE_LAPRAS = "Ice Zone Main Area - Ice Zone Lapras" => (3, 2, 0);
    BEACH_ZONE_LAPRAS_AREA_BEACH_ZONE_LAPRAS = "Beach Zone Lapras Area - Beach Zone Lapras" => (3, 1, 1);
    ICE_ZONE_MAIN_AREA_EMPOLEON_GATE = "Ice Zone Main Area - Empoleon Gate" => (3, 2, 1);
    ICE_ZONE_EMPOLEON_AREA_ICE_ZONE_MAIN_GATE = "Ice Zone Empoleon Area - Ice Zone Main Gate" => (3, 3, 0);
    CAVERN_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION = "Cavern Zone Main Area - Treehouse Connection" => (4, 1, 0);
    TREEHOUSE_CAVERN_PASSAGE_CAVERN_ZONE_CONNECTION = "Treehouse Cavern Passage - Cavern Zone Connection" => (2, 1, 2);
    CAVERN_ZONE_MAIN_AREA_MAGMA_ZONE_TRUCK = "Cavern Zone Main Area - Magma Zone Truck" => (4, 1, 1);
    MAGMA_ZONE_MAIN_AREA_CAVERN_ZONE_TRUCK = "Magma Zone Main Area - Cavern Zone Truck" => (4, 2, 0);
    MAGMA_ZONE_MAGCARGO_AREA_BLAZIKEN_GATE = "Magma Zone Magcargo Area - Blaziken Gate" => (4, 2, 1);
    MAGMA_ZONE_BLAZIKEN_AREA_MAIN_AREA_GATE = "Magma Zone Blaziken Area - Main Area Gate" => (4, 3, 0);
    HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION = "Haunted Zone Main Area - Treehouse Connection" => (5, 1, 0);
    TREEHOUSE_HAUNTED_PASSAGE_HAUNTED_ZONE_CONNECTION = "Treehouse Haunted Passage - Haunted Zone Connection" => (2, 1, 3);
    HAUNTED_ZONE_MAIN_AREA_MANSION_GATE = "Haunted Zone Main Area - Mansion Gate" => (5, 1, 1);
    HAUNTED_ZONE_MANSION_AREA_MAIN_AREA_GATE = "Haunted Zone Mansion Area - Main Area Gate" => (5, 2, 0);
    HAUNTED_ZONE_ROTOM_AREA_BOOKSHELF_AREA_CONNECTION = "Haunted Zone Rotom Area - Bookshelf Area Connection" => (5, 3, 0);
    HAUNTED_ZONE_BOOKSHELF_AREA_ROTOM_CONNECTION = "Haunted Zone Bookshelf Area - Rotom Connection" => (5, 2, 1);
    GRANITE_ZONE_MAIN_AREA_TREEHOUSE_CONNECTION = "Granite Zone Main Area - Treehouse Connection" => (6, 1, 0);
    TREEHOUSE_GRANITE_PASSAGE_GRANITE_ZONE_CONNECTION = "Treehouse Granite Passage - Granite Zone Connection" => (2, 1, 4);
    FLOWER_ZONE_MAIN_AREA_GRANITE_ZONE_GATE = "Flower Zone Main Area - Granite Zone Gate" => (6, 2, 0);
    GRANITE_ZONE_MAIN_AREA_FLOWER_ZONE_GATE = "Granite Zone Main Area - Flower Zone Gate" => (6, 1, 1);
    TREEHOUSE_PIPLUP_SKYBALLOON = "Treehouse - Piplup Skyballoon" => (2, 1, 6);
    SKYGARDEN_PIPLUP_SKYBALLOON = "Skygarden - Piplup Skyballoon" => (7, 1, 0);

    TREEHOUSE_MEADOW_DRIFBLIM_FAST_TRAVEL = "Treehouse - Meadow Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_BEACH_DRIFBLIM_FAST_TRAVEL = "Treehouse - Beach Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_ICE_DRIFBLIM_FAST_TRAVEL = "Treehouse - Ice Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_CAVERN_DRIFBLIM_FAST_TRAVEL = "Treehouse - Cavern Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_MAGMA_DRIFBLIM_FAST_TRAVEL = "Treehouse - Magma Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Treehouse - Haunted Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_GRANITE_DRIFBLIM_FAST_TRAVEL = "Treehouse - Granite Drifblim Fast Travel" => (2, 1, 5);
    TREEHOUSE_FLOWER_DRIFBLIM_FAST_TRAVEL = "Treehouse - Flower Drifblim Fast Travel" => (2, 1, 5);

    MEADOW_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Treehouse Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Beach Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Ice Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Cavern Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Magma Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Haunted Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Granite Drifblim Fast Travel" => (1, 1, 3);
    MEADOW_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Meadow Zone Main Area - Flower Drifblim Fast Travel" => (1, 1, 3);

    BEACH_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Meadow Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Treehouse Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Ice Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Cavern Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Magma Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Haunted Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Granite Drifblim Fast Travel" => (3, 1, 2);
    BEACH_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Beach Zone Main Area - Flower Drifblim Fast Travel" => (3, 1, 2);

    ICE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Meadow Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Treehouse Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Beach Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Cavern Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Magma Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Haunted Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Granite Drifblim Fast Travel" => (3, 2, 2);
    ICE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Ice Zone Main Area - Flower Drifblim Fast Travel" => (3, 2, 2);

    CAVERN_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Meadow Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Treehouse Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Beach Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Ice Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Magma Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Haunted Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Granite Drifblim Fast Travel" => (4, 1, 2);
    CAVERN_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Cavern Zone Main Area - Flower Drifblim Fast Travel" => (4, 1, 2);

    MAGMA_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Meadow Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Treehouse Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Beach Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Ice Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Cavern Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Haunted Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Granite Drifblim Fast Travel" => (4, 2, 2);
    MAGMA_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Magma Zone Main Area - Flower Drifblim Fast Travel" => (4, 2, 2);

    HAUNTED_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Meadow Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Treehouse Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Beach Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Ice Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Cavern Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Magma Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Granite Drifblim Fast Travel" => (5, 1, 2);
    HAUNTED_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Haunted Zone Main Area - Flower Drifblim Fast Travel" => (5, 1, 2);

    GRANITE_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Meadow Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Treehouse Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Beach Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Ice Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Cavern Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Magma Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Haunted Drifblim Fast Travel" => (6, 1, 2);
    GRANITE_ZONE_MAIN_AREA_FLOWER_DRIFBLIM_FAST_TRAVEL = "Granite Zone Main Area - Flower Drifblim Fast Travel" => (6, 1, 2);

    FLOWER_ZONE_MAIN_AREA_MEADOW_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Meadow Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_TREEHOUSE_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Treehouse Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_BEACH_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Beach Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_ICE_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Ice Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_CAVERN_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Cavern Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_MAGMA_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Magma Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_HAUNTED_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Haunted Drifblim Fast Travel" => (6, 2, 1);
    FLOWER_ZONE_MAIN_AREA_GRANITE_DRIFBLIM_FAST_TRAVEL = "Flower Zone Main Area - Granite Drifblim Fast Travel" => (6, 2, 1);
}

macro_rules! attraction_entrances {
    ($($name:ident = $entrance:literal;)+) => {
        pub(crate) fn attraction_config_prefix(entrance: &str) -> Option<&'static str> {
            match entrance {
                $($entrance => Some(stringify!($name)),)+
                _ => None,
            }
        }
    };
}

attraction_entrances! {
    MEADOW_ZONE_MAIN_AREA_BULBASAUR_ATTRACTION = "Meadow Zone Main Area - Bulbasaur Attraction";
    MEADOW_ZONE_VENUSAUR_AREA_VENUSAUR_ATTRACTION = "Meadow Zone Venusaur Area - Venusaur Attraction";
    BEACH_ZONE_MAIN_AREA_PELIPPER_ATTRACTION = "Beach Zone Main Area - Pelipper Attraction";
    BEACH_ZONE_RECYCLE_AREA_GYARADOS_ATTRACTION = "Beach Zone Recycle Area - Gyarados Attraction";
    ICE_ZONE_EMPOLEON_AREA_EMPOLEON_ATTRACTION = "Ice Zone Empoleon Area - Empoleon Attraction";
    CAVERN_ZONE_MAIN_AREA_BASTIODON_ATTRACTION = "Cavern Zone Main Area - Bastiodon Attraction";
    MAGMA_ZONE_CIRCLE_AREA_RHYPERIOR_ATTRACTION = "Magma Zone Circle Area - Rhyperior Attraction";
    MAGMA_ZONE_BLAZIKEN_AREA_BLAZIKEN_ATTRACTION = "Magma Zone Blaziken Area - Blaziken Attraction";
    HAUNTED_ZONE_MAIN_AREA_TANGROWTH_ATTRACTION = "Haunted Zone Main Area - Tangrowth Attraction";
    HAUNTED_ZONE_MANSION_AREA_DUSKNOIR_ATTRACTION = "Haunted Zone Mansion Area - Dusknoir Attraction";
    HAUNTED_ZONE_ROTOM_AREA_ROTOM_ATTRACTION = "Haunted Zone Rotom Area - Rotom Attraction";
    GRANITE_ZONE_MAIN_AREA_ABSOL_ATTRACTION = "Granite Zone Main Area - Absol Attraction";
    GRANITE_ZONE_MAIN_AREA_SALAMENCE_ATTRACTION = "Granite Zone Main Area - Salamence Attraction";
    FLOWER_ZONE_MAIN_AREA_RAYQUAZA_ATTRACTION = "Flower Zone Main Area - Rayquaza Attraction";
}

macro_rules! attraction_ids {
    ($($name:ident = $exit:literal => $id:literal;)+) => {
        pub(crate) fn attraction_id(exit: &str) -> Option<i32> {
            match exit {
                $($exit => Some($id),)+
                _ => None,
            }
        }
    };
}

attraction_ids! {
    BULBASAUR_S_DARING_DASH_ATTRACTION_ATTRACTION_MENU = "Bulbasaur's Daring Dash Attraction - Attraction Menu" => 0xf;
    VENUSAUR_S_VINE_SWING_ATTRACTION_ATTRACTION_MENU = "Venusaur's Vine Swing Attraction - Attraction Menu" => 0x2;
    PELIPPER_S_CIRCLE_CIRCUIT_ATTRACTION_ATTRACTION_MENU = "Pelipper's Circle Circuit Attraction - Attraction Menu" => 0x6;
    GYARADOS_AQUA_DASH_ATTRACTION_ATTRACTION_MENU = "Gyarados' Aqua Dash Attraction - Attraction Menu" => 0x5;
    EMPOLEON_S_SNOW_SLIDE_ATTRACTION_ATTRACTION_MENU = "Empoleon's Snow Slide Attraction - Attraction Menu" => 0x8;
    BASTIODON_S_PANEL_CRUSH_ATTRACTION_ATTRACTION_MENU = "Bastiodon's Panel Crush Attraction - Attraction Menu" => 0x9;
    RHYPERIOR_S_BUMPER_BURN_ATTRACTION_ATTRACTION_MENU = "Rhyperior's Bumper Burn Attraction - Attraction Menu" => 0xa;
    BLAZIKEN_S_BOULDER_BASH_ATTRACTION_ATTRACTION_MENU = "Blaziken's Boulder Bash Attraction - Attraction Menu" => 0xb;
    DUSKNOIR_S_SPEED_SLAM_ATTRACTION_ATTRACTION_MENU = "Dusknoir's Speed Slam Attraction - Attraction Menu" => 0x4;
    TANGROWTH_S_SWING_ALONG_ATTRACTION_ATTRACTION_MENU = "Tangrowth's Swing-Along Attraction - Attraction Menu" => 0x3;
    ROTOM_S_SPOOKY_SHOOT_EM_UP_ATTRACTION_ATTRACTION_MENU = "Rotom's Spooky Shoot-'em-Up Attraction - Attraction Menu" => 0xc;
    ABSOL_S_HURDLE_BOUNCE_ATTRACTION_ATTRACTION_MENU = "Absol's Hurdle Bounce Attraction - Attraction Menu" => 0x0;
    SALAMENCE_S_SKY_RACE_ATTRACTION_ATTRACTION_MENU = "Salamence's Sky Race Attraction - Attraction Menu" => 0xe;
    RAYQUAZA_S_BALLOON_PANIC_ATTRACTION_ATTRACTION_MENU = "Rayquaza's Balloon Panic Attraction - Attraction Menu" => 0x1;
}
