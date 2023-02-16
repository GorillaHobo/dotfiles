return {
    cs = {
        { type = "coreclr",
            name = "launch - netcoredbg",
            request = "launch",
            program = function()
                return vim.fn.input('Path to dll', vim.fn.getcwd() .. '/bin/Debug/net6.0/*.dll', 'file')
            end,
        }
    }
}
