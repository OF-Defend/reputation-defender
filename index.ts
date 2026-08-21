#!/usr/bin/env node

interface ReputationDefenderInput {
  brand: string;
  defenseType: string;
  riskScore: number;
  trustSignalScore: number;
  searchDefenseScore: number;
  profileDefenseScore: number;
  reviewDefenseScore: number;
  listingDefenseScore: number;
}

interface ReputationDefenderOutput {
  brand: string;
  defenseType: string;
  riskScore: number;
  trustSignalScore: number;
  searchDefenseScore: number;
  profileDefenseScore: number;
  reviewDefenseScore: number;
  listingDefenseScore: number;
  overallDefenseIndex: number;
  priorityAction: string;
  defenseChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function formatDefenseType(defenseType: string): string {
  return defenseType.split("-").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" ");
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    risk: "Risk",
    trustSignal: "Trust Signal",
    searchDefense: "Search Defense",
    profileDefense: "Profile Defense",
    reviewDefense: "Review Defense",
    listingDefense: "Listing Defense",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getDefenseChannels(search: number, profile: number, review: number, listing: number): Record<string, number> {
  return {
    "Search Results": Math.min(100, Math.round(search * 1.0)),
    "Social Profiles": Math.min(100, Math.round(profile * 1.0)),
    "Review Platforms": Math.min(100, Math.round(review * 1.0)),
    "Business Listings": Math.min(100, Math.round(listing * 1.0)),
  };
}

export function runReputationDefender(input: ReputationDefenderInput): ReputationDefenderOutput {
  const scores = {
    risk: input.riskScore,
    trustSignal: input.trustSignalScore,
    searchDefense: input.searchDefenseScore,
    profileDefense: input.profileDefenseScore,
    reviewDefense: input.reviewDefenseScore,
    listingDefense: input.listingDefenseScore,
  };
  const overallDefenseIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    brand: input.brand,
    defenseType: formatDefenseType(input.defenseType),
    riskScore: input.riskScore,
    trustSignalScore: input.trustSignalScore,
    searchDefenseScore: input.searchDefenseScore,
    profileDefenseScore: input.profileDefenseScore,
    reviewDefenseScore: input.reviewDefenseScore,
    listingDefenseScore: input.listingDefenseScore,
    overallDefenseIndex,
    priorityAction: getPriorityAction(scores),
    defenseChannels: getDefenseChannels(input.searchDefenseScore, input.profileDefenseScore, input.reviewDefenseScore, input.listingDefenseScore),
  };
}

const args = process.argv.slice(2);
const brand = args[0] || "brand-name";
const defenseType = args[1] || "full-defense";
const riskScore = parseInt(args[2]) || 88;
const trustSignalScore = parseInt(args[3]) || 82;
const searchDefenseScore = parseInt(args[4]) || 85;
const profileDefenseScore = parseInt(args[5]) || 78;
const reviewDefenseScore = parseInt(args[6]) || 90;
const listingDefenseScore = parseInt(args[7]) || 84;

const result = runReputationDefender({
  brand, defenseType, riskScore, trustSignalScore,
  searchDefenseScore, profileDefenseScore, reviewDefenseScore, listingDefenseScore,
});

console.log(`Brand: ${result.brand}`);
console.log(`Defense Type: ${result.defenseType}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Risk Score:                    ${result.riskScore}/100  [${getStatus(result.riskScore)}]`);
console.log(`Trust Signal Score:            ${result.trustSignalScore}/100  [${getStatus(result.trustSignalScore)}]`);
console.log(`Search Defense Score:          ${result.searchDefenseScore}/100  [${getStatus(result.searchDefenseScore)}]`);
console.log(`Profile Defense Score:         ${result.profileDefenseScore}/100  [${getStatus(result.profileDefenseScore)}]`);
console.log(`Review Defense Score:          ${result.reviewDefenseScore}/100  [${getStatus(result.reviewDefenseScore)}]`);
console.log(`Listing Defense Score:         ${result.listingDefenseScore}/100  [${getStatus(result.listingDefenseScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Defense Index:         ${result.overallDefenseIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nDefense Channels:");
Object.entries(result.defenseChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(22)} ${score}/100`);
});
