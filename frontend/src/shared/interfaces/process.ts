export interface Iprocess {
  id: string;
  arrival: number;
  duration: number;
  priority: number;
  quantum?: number;
  aging?: number;
}

export interface Isimulation {
  algorithm: string;
  processes: Iprocess[];
}

export interface ItimelineEntry {
  time: string;
  state: Record<string, string>;
}

export interface Iresult {
  average_turnaround: number;
  average_waiting: number;
  context_switches: number;
  timeline: ItimelineEntry[];
}
