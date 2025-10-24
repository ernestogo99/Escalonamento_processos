import { TextField, type TextFieldProps } from "@mui/material";
import { styled } from "@mui/material/styles";

export const CustomTextField = styled(TextField)<TextFieldProps>(
  ({ theme }) => ({
    "& label.Mui-focused": {
      color: "#ff69b4",
    },
    "& .MuiOutlinedInput-root": {
      "& fieldset": {
        borderColor: "#ccc",
      },
      "&:hover fieldset": {
        borderColor: "#ff69b4",
      },
      "&.Mui-focused fieldset": {
        borderColor: "#ff69b4",
      },
    },
    "& .MuiInputBase-input": {
      color: "#fff",
    },
    "& .MuiInputLabel-root": {
      color: "#ccc",
    },
  })
);
