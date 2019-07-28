`timescale 1us/1ns

// Testbench ------------------------------------------------

module dda_testbench();
  reg  clk, reset;
  reg  [31:0] dt, y0;
  wire [31:0] t, y, dy;

  dda dut(
    .clk  (clk),
    .reset(reset),
    .dt   (dt),
    .y0   (y0),
    .t    (t),
    .y    (y),
    .dy   (dy)
  );

  always begin
    clk <= 1; #5; clk <= 0; #5;
  end

  initial begin
    $dumpfile("dda.vcd");
    $dumpvars(0, dda_testbench);

    reset <= 1;
    y0    <= 1 <<< 16;  // 1.0 in Q16.16

    @(negedge clk);
    reset <= 0;

    repeat(513)
      @(posedge clk);

    $display("t = %b", t);
    $display("t = %d", t/65536);
    $display("y = %b", y);
    $display("y = %d", y/65536);

    $finish;
  end
endmodule

// Top ------------------------------------------------------

module dda(input         clk,
           input         reset,
           input  [31:0] dt,
           input  [31:0] y0,
           output [31:0] t,
           output [31:0] y,
           output [31:0] dy);
  reg  [31:0] t, y, dy;
  wire [31:0] y_next, dy_next;

  deriv deriv(y, dy_next);
  integral integral(y, dy, y_next);

  always @(posedge clk) begin
    if (reset) begin
      t  <= 0;
      y  <= y0;
      dy <= 0;
    end
    else begin
      // dt is 2e-9, so in Q16.16 this is 1 << (16-9)
      t  <= t + (1 <<< 7);
      y  <= y_next;
      dy <= dy_next;
    end
  end
endmodule

// simple ODE: dy/dt = y
module deriv(input  [31:0] y,
             output [31:0] dy);
  assign dy = y;
endmodule

// forward euler
module integral(input  [31:0] y,
                input  [31:0] dy,
                output [31:0] y_next);
  assign y_next = y + (dy >>> 9);
endmodule

// multiplies two signed Qn.m fixed point numbers
module signed_mult #(
  parameter n = 16,
  parameter m = 16
)(
  input  signed [in_size-1:0] a, b,
  output signed [in_size-1:0] result
);

  localparam in_size = n + m;
  localparam out_size = 2 * in_size;
  
  wire signed [out_size-1:0] mult;

  assign mult = a * b;
  assign result = {mult[out_size-1], mult[out_size-n-2:m]};
endmodule
