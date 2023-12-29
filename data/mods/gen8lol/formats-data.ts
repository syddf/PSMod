// TODO: alphabetize move names. I'm trying to implement this on a low-quality laptop under time pressure, so I haven't bothered doing so.
export const FormatsData: {[k: string]: ModdedSpeciesFormatsData} = {
	bulbasaur: {
		tier: "OU",
	},
	ivysaur: {
		tier: "OU",
	},
	venusaur: {
		tier: "RU",
		doublesTier: "DUU",
	},
	arceusbug: {
	},
	arceusdark: {
	},
	arceusdragon: {
	},
	arceuselectric: {
	},
	arceusfairy: {
	},
	arceusfighting: {
	},
	arceusfire: {
	},
	arceusflying: {
	},
	arceusghost: {
	},
	arceusgrass: {
	},
	arceusground: {
	},
	arceusice: {
	},
	arceuspoison: {
	},
	arceuspsychic: {
	},
	arceusrock: {
	},
	arceussteel: {
	},
	arceuswater: {
	},
	// Because it's marked as Unobtainable in the main file for some reason
	eternatuseternamax: {
		inherit: true,
		isNonstandard: "Past",
	},
};
