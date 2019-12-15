
import asyncio
from rtlsdr import RtlSdr
import PIPE
import io.StringIO

from pylab import *
from rtlsdr import *

from rtlsdr import RtlSdr
async def _read_stream(stream, cb):


async def _stream_subprocess(sdr, stdout_cb, stderr_cb):
    process = await sdr.stream().create_subprocess_exec(*cmd,
    stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

await asyncio.wait([
    _read_stream(process.stdout, stdout_cb),
    _read_stream(process.stderr, stderr_cb)
])
return await process.wait()


def execute(cmd, stdout_cb, stderr_cb):
    # configure device
    sdr=RtlSdr()
sdr.sample_rate = 2.4e6
sdr.center_freq = 101e5
sdr.gain = 4
sample = sdr.read_samples(256*1024)
psd(sample, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
xlabel('Frequency (MHz)')
ylabel('Relative power (dB)')
show()
cmd = ()
loop = asyncio.get_event_loop()
rc = loop.run_until_complete(
    _stream_subprocess(
        cmd,
        stdout_cb,
        stderr_cb,
    ))
loop.close()
return rc

if __name__ == '__main__':
    print(execute(
        ["bash", "-c", "echo stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done"],
        lambda x: print("STDOUT: %s" % x),
        lambda x: print("STDERR: %s" % x),
    ))



    async for samples in sdr.stream():
        StringIO.write(samples)
    # to stop streaming:
await sdr.stop()
# done
sdr.close()

loop = asyncio.get_event_loop()
loop.connect_write_pipe(protocol_factory, PIPE.)
loop.run_until_complete(streaming())


try:
    # simulate large output (your code replaces this loop)
    for x in range(10000):
        print("y")
    # flush output here to force SIGPIPE to be triggered
    # while inside this try block.
    sys.stdout.flush()
except BrokenPipeError:
    # Python flushes standard streams on exit; redirect remaining output
    # to devnull to avoid another BrokenPipeError at shutdown
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.exit(1)  # Python exits with error code 1 on EPIPE