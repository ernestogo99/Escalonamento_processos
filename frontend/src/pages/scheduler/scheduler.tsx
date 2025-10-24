import {
  Box,
  Typography,
  FormControl,
  MenuItem,
  Stack,
  Button,
  IconButton,
  type SelectChangeEvent,
  Select,
} from "@mui/material";
import { Add, Close } from "@mui/icons-material";
import { useState } from "react";
import type { Iprocess } from "../../shared/interfaces/process";
import { CustomTextField } from "../../shared/components";

export const Scheduler = () => {
  const [algorithm, setAlgorithm] = useState<string>("fcfs");
  const [processes, setProcesses] = useState<Iprocess[]>([]);
  const [quantum, setQuantum] = useState<Number>();
  const [aging, setAging] = useState<Number>();

  const handleAlgorithmChange = (event: SelectChangeEvent) => {
    setAlgorithm(event.target.value as string);
  };

  const handleAddProcess = () => {
    const newProcess: Iprocess = {
      id: `P${processes.length + 1}`,
      arrival: 0,
      duration: 1,
      priority: 1,
    };
    setProcesses([...processes, newProcess]);
  };

  const handleRemoveProcess = () => {
    setProcesses(processes.slice(0, -1));
  };

  const handleChange = (
    index: number,
    field: keyof Iprocess,
    value: string | number
  ) => {
    const updated = [...processes];
    // @ts-ignore
    updated[index][field] = Number(value) ?? value;
    setProcesses(updated);
  };

  const handleStartSimulation = () => {
    console.log({ algorithm, processes });
  };

  return (
    <Box
      sx={{
        backgroundColor: "#2b2d42",
        color: "#fff",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <Typography variant="h4" fontWeight="bold" mb={10}>
        Process Scheduler
      </Typography>

      <Stack spacing={2} width="50%">
        <FormControl fullWidth>
          <Typography mb={1} fontWeight="bold">
            Algorithm
          </Typography>

          <Select
            value={algorithm}
            onChange={handleAlgorithmChange}
            sx={{
              color: "#fff",
              "& .MuiOutlinedInput-notchedOutline": {
                borderColor: "#ccc",
              },
              "&:hover .MuiOutlinedInput-notchedOutline": {
                borderColor: "#ff69b4",
              },
              "&.Mui-focused .MuiOutlinedInput-notchedOutline": {
                borderColor: "#ff69b4",
              },
              "& .MuiSelect-icon": {
                color: "#fff",
              },
            }}
          >
            <MenuItem value="fcfs">First Come First Served (FCFS)</MenuItem>
            <MenuItem value="sjf">Shortest Job First (SJF)</MenuItem>
            <MenuItem value="srtf">
              Shortest Remaining Time First (SRTF)
            </MenuItem>
            <MenuItem value="pnp">Priority (Non-Preemptive)</MenuItem>
            <MenuItem value="pp">Priority (Preemptive)</MenuItem>
            <MenuItem value="rr">Round Robin</MenuItem>
            <MenuItem value="rr_priority_aging">
              Round Robin (Priority + Aging)
            </MenuItem>
          </Select>
        </FormControl>

        {["rr", "rr_priority_aging"].includes(algorithm) && (
          <>
            <Typography fontWeight="bold">Quantum</Typography>
            <CustomTextField
              type="number"
              value={quantum}
              onChange={(e) => setQuantum(Number(e.target.value))}
              size="small"
            />
          </>
        )}

        {["rr_priority_aging"].includes(algorithm) && (
          <>
            <Typography fontWeight="bold">Aging</Typography>
            <CustomTextField
              type="number"
              value={aging}
              onChange={(e) => setAging(Number(e.target.value))}
              size="small"
            />
          </>
        )}

        <Typography fontWeight="bold" color="#f8f8f8">
          Processes
        </Typography>

        {processes.map((p, index) => (
          <Stack
            key={p.id}
            direction="row"
            alignItems="center"
            justifyContent="space-between"
          >
            <CustomTextField label="Id" value={p.id} size="small" disabled />
            <CustomTextField
              label="Arrival"
              type="number"
              value={p.arrival}
              onChange={(e) =>
                handleChange(index, "arrival", Number(e.target.value))
              }
              size="small"
            />
            <CustomTextField
              label="Burst"
              type="number"
              value={p.duration}
              onChange={(e) =>
                handleChange(index, "duration", Number(e.target.value))
              }
              size="small"
            />
            {["pnp", "pp", "rr_priority_aging"].includes(algorithm) && (
              <CustomTextField
                label="Priority"
                type="number"
                value={p.priority}
                onChange={(e) =>
                  handleChange(index, "priority", Number(e.target.value))
                }
                size="small"
              />
            )}
          </Stack>
        ))}

        <Stack direction="row" spacing={2} justifyContent="center">
          <IconButton
            color="primary"
            onClick={handleAddProcess}
            sx={{ bgcolor: "#ff69b4", color: "#fff" }}
          >
            <Add />
          </IconButton>
          <IconButton
            onClick={handleRemoveProcess}
            sx={{
              bgcolor: "#ff4444",
              color: "#fff",
              "&:hover": { opacity: 0.9 },
            }}
          >
            <Close />
          </IconButton>
        </Stack>

        <Button
          variant="contained"
          fullWidth
          sx={{ mt: 2, bgcolor: "#ff69b4", color: "#000", fontWeight: "bold" }}
          onClick={handleStartSimulation}
        >
          START SIMULATION
        </Button>
      </Stack>
    </Box>
  );
};
