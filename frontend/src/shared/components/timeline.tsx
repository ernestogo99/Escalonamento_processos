// src/components/TimelineDialog.tsx
import {
  Box,
  Typography,
  Dialog,
  DialogContent,
  DialogTitle,
  IconButton,
  Tooltip,
  Stack,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import type { Iresult } from "../interfaces/process";

interface TimelineDialogProps {
  open: boolean;
  onClose: () => void;
  result: Iresult | null;
}

export const TimelineDialog = ({
  open,
  onClose,
  result,
}: TimelineDialogProps) => {
  if (!result) return null;

  const colors = [
    "#b388eb",
    "#f38ba0",
    "#a1c181",
    "#f6bd60",
    "#84a59d",
    "#f28482",
  ];

  return (
    <Dialog
      open={open}
      onClose={onClose}
      maxWidth="md"
      fullWidth
      PaperProps={{
        sx: {
          bgcolor: "#1c1c28",
          color: "#fff",
          borderRadius: 4,
          p: 2,
        },
      }}
    >
      <DialogTitle
        sx={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          fontWeight: "bold",
        }}
      >
        Scheduler
        <IconButton onClick={onClose} sx={{ color: "#fff" }}>
          <CloseIcon />
        </IconButton>
      </DialogTitle>

      <DialogContent>
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            height: 50,
            borderRadius: 2,
            overflow: "hidden",
            border: "1px solid #444",
            mb: 2,
          }}
        >
          {result.timeline.map((entry, idx) => {
            const runningProcessId = Object.entries(entry.state).find(
              ([_, status]) => status === "##"
            )?.[0];

            return (
              <Tooltip
                key={idx}
                title={`t=${entry.time} - ${
                  runningProcessId ? runningProcessId : "idle"
                }`}
              >
                <Box
                  sx={{
                    flexBasis: `${100 / result.timeline.length}%`,
                    height: "100%",
                    bgcolor: runningProcessId
                      ? colors[
                          parseInt(runningProcessId.replace("P", "")) %
                            colors.length
                        ]
                      : "#555",
                    transition: "background 0.3s",
                  }}
                />
              </Tooltip>
            );
          })}
        </Box>

        {/* Estatísticas */}
        <Stack
          direction={{ xs: "column", sm: "row" }}
          spacing={2}
          justifyContent="center"
          textAlign="center"
        >
          <Typography>
            ⏱ Average Wait Time: {result.average_waiting.toFixed(2)}
          </Typography>
          <Typography>
            ⏱ Average TurnAround Time: {result.average_turnaround.toFixed(2)}
          </Typography>
          <Typography>Context switches: {result.context_switches}</Typography>
        </Stack>
      </DialogContent>
    </Dialog>
  );
};
