import type { Isimulation, Iresult } from "../interfaces";
import { api } from "./axiosconfig/config";

const scheduleTask = async (
  simulation: Isimulation
): Promise<Iresult | Error> => {
  try {
    const { data } = await api.post("/scheduling/schedule", simulation);
    if (data) {
      return data;
    }
    return new Error("Error with task simulation");
  } catch (error: any) {
    console.error(error);
    return new Error("Error with task simulation");
  }
};

export const scheduleService = {
  scheduleTask,
};
