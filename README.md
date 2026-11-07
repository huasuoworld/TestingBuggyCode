# TestingBuggyCode, Markdown plugin(Markdown Preview Mermaid Support)


```mermaid
graph TD;
    white_box_testing --> syntax_error;
    white_box_testing --> runtime_error;
    white_box_testing --> logic_error;

    syntax_error --> testing_program_with_pytest;
    syntax_error --> through_the_complier_VSCode;

    runtime_error --> runing_unittest_with_pytest;

    logic_error --> calculate_total;
    logic_error --> apply_discount;
    logic_error --> add_item;
    logic_error --> integration_testing;

    calculate_total --> cheking_operators;
    apply_discount --> checking_if_branch;
    add_item --> checking_typing;
    integration_testing --> checking_if_branch;

    testing_program_with_pytest --> syntax_error_line16;
    testing_program_with_pytest --> syntax_error_line28;

    syntax_error_line16 --> fill_missing_symbols;
    syntax_error_line28 --> fill_missing_symbols;

    runing_unittest_with_pytest --> attribute_error;
    attribute_error --> change_itemz_to_items;

    cheking_operators --> operator_error;operator_error --> change_plus_to_multiply;

    checking_if_branch --> missing_else_statement;missing_else_statement --> fill_missing_else_statement;

    add_item --> typing_error;
    typing_error --> converting_typing;
```