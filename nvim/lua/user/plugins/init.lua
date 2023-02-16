-- Configure plugins
return {
        ["sainnhe/gruvbox-material"] = {},

        ["kylechui/nvim-surround"] = {
                config = function()
                        require("nvim-surround").setup()
                end
        },

        ["nanotee/sqls.nvim"] = {
                module = { "sqls" },
                cmd = {
                        "SqlsExecuteQuery",
                        "SqlsExecuteQueryVertical",
                        "SqlsShowDatabases",
                        "SqlsShowSchemas",
                        "SqlsShowConnections",
                        "SqlsSwitchDatabase",
                        "SqlsSwitchConnection",
                },
        },

        ["wellle/targets.vim"] = {},

        -- ['dgrbrady/nvim-docker'] = {
        --         requires = { 'nvim-lua/plenary.nvim', 'MunifTanjim/nui.nvim' },
        --         -- rocks = '4O4/reactivex', -- ReactiveX Lua implementation
        -- }
        --
        -- You can disable default plugins as follows:
        -- ["goolord/alpha-nvim"] = { disable = true },

        -- You can also add new plugins here as well:
        -- Add plugins, the packer syntax without the "use"
        -- { "andweeb/presence.nvim" },
        -- {
        --   "ray-x/lsp_signature.nvim",
        --   event = "BufRead",
        --   config = function()
        --     require("lsp_signature").setup()
        --   end,
        -- },
        --

        -- We also support wa key value style plugin definition similar to NvChad:
        -- ["ray-x/lsp_signature.nvim"] = {
        --   event = "BufRead",
        --   config = function()
        --     require("lsp_signature").setup()
        --   end,
        -- },
}
