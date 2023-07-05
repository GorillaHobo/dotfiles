return {
  n = {
    ["<leader>bn"] = { "<cmd>tabnew<cr>", desc = "New tab" },
    ["<leader>bD"] = {
      function()
        require("astronvim.utils.status").heirline.buffer_picker(
          function(bufnr) require("astronvim.utils.buffer").close(bufnr) end
        )
      end,
      desc = "Pick to close",
    },
    ["<leader>b"] = { name = "Buffers" },
    ["<S-h>"] = {
      function() require("astronvim.utils.buffer").nav(-(vim.v.count > 0 and vim.v.count or 1)) end,
      desc = "Next buffer",
    },
    ["<S-l>"] = {
      function() require("astronvim.utils.buffer").nav((vim.v.count > 0 and vim.v.count or 1)) end,
      desc = "Next buffer",
    },
    ["<leader>fs"] = { ":w!<cr>", desc = "I don't know" },
    ["J"] = { "mzJ`z" },
    ["<C-d>"] = { "<C-d>zz" },
    ["<C-u>"] = { "<C-u>zz" },
    ["n"] = { "nzzzv" },
    ["N"] = { "Nzzzv" },
    ["<leader>y"] = { [["+y]] },
    ["<leader>Y"] = { [["+Y]] },
    ["<leader>d"] = { [["_d]] },
    -- toggle lazydocker
    ["<leader>td"] = {
      function()
        if vim.fn.executable "lazydocker" == 1 then require("astronvim.utils").toggle_term_cmd "lazydocker" end
      end,
      desc = "ToggleTerm lazydocker",
    },
  },
  t = {
    -- setting a mapping to false will disable it
    -- ["<esc>"] = false,
  },
  v = {
    ["J"] = { ":m '>+1<CR>gv=gv" },
    ["K"] = { ":m '<-2<CR>gv=gv" },
    ["<leader>y"] = { [["+y]] },
  },
  i = {
    ["<C-f>"] = { "<Right>" },
    ["<C-b>"] = { "<Left>" },
  },
  x = {
    ["<leader>p"] = { [["_dP]] },
  },
}
