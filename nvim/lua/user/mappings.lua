-- Mapping data with "desc" stored directly by vim.keymap.set().
--
-- Please use this mappings table to set keyboard mapping since this is the
-- lower level configuration and more robust one. (which-key will
-- automatically pick-up stored data by this setting.)

return {
    n = {
        ["<leader>fs"] = { ":w!<cr>", desc = "I don't know" },
        ["J"] = { "mzJ`z" },

        ["<C-d>"] = { "<C-d>zz" },
        ["<C-u>"] = { "<C-u>zz" },

        ["n"] = { "nzzzv" },
        ["N"] = { "Nzzzv" },

        ["<leader>y"] = { [["+y]] },
        ["<leader>Y"] = { [["+Y]] },

        ["<leader>d"] = { [["_d]] },
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

    t = {
        -- setting a mapping to false will disable it
        -- ["<esc>"] = false,
    },

}
