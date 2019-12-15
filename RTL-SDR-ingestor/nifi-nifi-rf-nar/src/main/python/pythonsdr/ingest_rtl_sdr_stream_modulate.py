import asyncio
import sys
import os
import os.PIPE as PIPE
import yaml

#############################################################
#rtl_sdr, an I/Q recorder for RTL2832 based DVB-T receivers #
#############################################################
#Usage:	 -f frequency_to_tune_to [Hz]
#[-s samplerate (default: 2048000 Hz)]
#[-d device_index (default: 0)]
#[-g gain (default: 0 for auto)]
#[-p ppm_error (default: 0)]
#[-b output_block_size (default: 16 * 16384)]
#[-n number of samples to read (default: 0, infinite)]
#[-S force sync output (default: async)]
#filename (a '-' dumps samples to stdout)

# see ${project.home}/conf/sdr-scanner.yaml for configuration




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
    config=dict()

    with open("sdr-scanner.yaml", 'r') as stream:
        try:
            config = yaml.load([stream])
        except yaml.YAMLError as exc:
            print(exc)

    from pyrtlsdr import RtlSdr

    sdr = RtlSdr()
    sdr.sample_rate = config.get(sample_rate, 2.4e6)
    sdr.center_freq = 101e5
    sdr.gain = 4
    sample = sdr.read_samples(256*1024)
   # psd(sample, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    cmd = ()
    try:
        # flush output here to force SIGPIPE to be triggered
        # while inside this try block.
        sys.stdout.flush()
    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)  # Python exits with error code 1 on EPIPE

        loop.close()
        return rc


    async for samples in sdr.stream():
        from io import StringIO

        if samples != None:
            StringIO.write(samples)
        # to stop streaming:
        await sdr.stop()
    # done
    sdr.close()

loop = asyncio.get_event_loop()
loop.connect_write_pipe(protocol_factory, PIPE.)
loop.run_until_complete(streaming())



if __name__ == '__main__':
    #print(execute(
    #    ["bash", "-c", "echo stdout && sleep 1 && echo stderr 1>&2 && sleep 1 && echo done"],
    #    lambda x: print("STDOUT: %s" % x),
    #    lambda x: print("STDERR: %s" % x),
    #    )
    #)
    execute("")


